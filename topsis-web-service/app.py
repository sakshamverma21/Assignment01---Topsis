from flask import Flask, render_template, request, flash, redirect, url_for
import pandas as pd
import numpy as np
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
import re
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'default-secret-key-change-this')
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['RESULT_FOLDER'] = 'results'

# Create folders if they don't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['RESULT_FOLDER'], exist_ok=True)

def validate_email(email):
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def topsis_calculation(file_path, weights, impacts):
    """Perform TOPSIS calculation"""
    # Read CSV
    df = pd.read_csv(file_path)
    
    if df.shape[1] < 3:
        raise ValueError("File must contain at least 3 columns")
    
    # Extract data (excluding first column)
    data = df.iloc[:, 1:]
    
    # Check for numeric values
    for col in data.columns:
        if not pd.api.types.is_numeric_dtype(data[col]):
            raise ValueError("Non-numeric values found in data")
    
    # Normalize
    norm = data / np.sqrt((data**2).sum())
    
    # Apply weights
    for i in range(len(weights)):
        norm.iloc[:, i] *= weights[i]
    
    # Determine ideal best and worst
    ideal_best = []
    ideal_worst = []
    
    for i in range(len(weights)):
        col = norm.iloc[:, i]
        if impacts[i] == '+':
            ideal_best.append(col.max())
            ideal_worst.append(col.min())
        else:
            ideal_best.append(col.min())
            ideal_worst.append(col.max())
    
    # Calculate distances
    dist_best = np.sqrt(((norm - ideal_best)**2).sum(axis=1))
    dist_worst = np.sqrt(((norm - ideal_worst)**2).sum(axis=1))
    
    # Calculate TOPSIS score
    score = dist_worst / (dist_best + dist_worst)
    
    # Add results to dataframe
    df['Topsis Score'] = score.values
    df['Rank'] = score.rank(ascending=False).astype(int).values
    
    return df

def send_email(to_email, result_file):
    """Send result file via email"""
    from_email = os.getenv('EMAIL_USER')
    password = os.getenv('EMAIL_PASSWORD')
    
    if not from_email or not password:
        raise ValueError("Email credentials not configured. Please set EMAIL_USER and EMAIL_PASSWORD in .env file")
    
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = 'TOPSIS Analysis Results'
    
    body = """
    Hello,
    
    Your TOPSIS analysis has been completed successfully.
    Please find the results attached.
    
    Best regards,
    TOPSIS Web Service
    """
    
    msg.attach(MIMEText(body, 'plain'))
    
    # Attach result file
    with open(result_file, 'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(result_file)}')
        msg.attach(part)
    
    # Send email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, password)
    server.send_message(msg)
    server.quit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        # Get form data
        file = request.files.get('file')
        weights_str = request.form.get('weights', '').strip()
        impacts_str = request.form.get('impacts', '').strip()
        email = request.form.get('email', '').strip()
        
        # Validate inputs
        if not file or file.filename == '':
            flash('Please select a file', 'error')
            return redirect(url_for('index'))
        
        if not weights_str or not impacts_str or not email:
            flash('All fields are required', 'error')
            return redirect(url_for('index'))
        
        # Validate email
        if not validate_email(email):
            flash('Invalid email format', 'error')
            return redirect(url_for('index'))
        
        # Parse weights and impacts
        try:
            weights = [float(w.strip()) for w in weights_str.split(',')]
            impacts = [i.strip() for i in impacts_str.split(',')]
        except ValueError:
            flash('Invalid weights format. Use comma-separated numbers.', 'error')
            return redirect(url_for('index'))
        
        # Validate impacts
        for impact in impacts:
            if impact not in ['+', '-']:
                flash('Impacts must be + or -', 'error')
                return redirect(url_for('index'))
        
        # Validate counts match
        if len(weights) != len(impacts):
            flash(f'Number of weights ({len(weights)}) must equal number of impacts ({len(impacts)})', 'error')
            return redirect(url_for('index'))
        
        # Save uploaded file
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        
        # Perform TOPSIS
        result_df = topsis_calculation(file_path, weights, impacts)
        
        # Save result
        result_filename = f'result_{file.filename}'
        result_path = os.path.join(app.config['RESULT_FOLDER'], result_filename)
        result_df.to_csv(result_path, index=False)
        
        # Send email
        send_email(email, result_path)
        
        # Clean up uploaded file
        os.remove(file_path)
        
        flash('Analysis completed! Results sent to your email.', 'success')
        return redirect(url_for('index'))
        
    except Exception as e:
        flash(f'Error: {str(e)}', 'error')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
