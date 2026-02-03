# TOPSIS Web Service

A Flask-based web service for TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) analysis.

## Features

- ✅ Upload CSV files for analysis
- ✅ Input weights and impacts via web form
- ✅ Email validation
- ✅ Automatic result delivery via email
- ✅ Clean and simple UI

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd topsis-web-service
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment variables:
   - Copy `.env.example` to `.env`:
     ```bash
     cp .env.example .env
     ```
   - Edit `.env` file with your credentials:
     ```
     EMAIL_USER=your-email@gmail.com
     EMAIL_PASSWORD=your-app-password
     SECRET_KEY=your-random-secret-key
     ```

**For Gmail App Password:**
- Go to Google Account → Security
- Enable 2-Step Verification
- Search "App passwords" → Generate new → Copy it
- Paste it as `EMAIL_PASSWORD` in `.env`

**Important:** Never commit the `.env` file to GitHub! It's already in `.gitignore`.

## Usage

1. Run the application:
```bash
python app.py
```

2. Open your browser and go to:
```
http://127.0.0.1:5000
```

3. Fill in the form:
   - **File Name**: Upload CSV file
   - **Weights**: Comma-separated weights (e.g., 1,1,1,1)
   - **Impacts**: Comma-separated + or - (e.g., +,+,-,+)
   - **Email Id**: Your email address

4. Click Submit and check your email for results!

## Validation Rules

- ✅ Number of weights must equal number of impacts
- ✅ Impacts must be + or -
- ✅ Email format must be valid
- ✅ CSV must contain numeric values (except first column)
- ✅ File must have at least 3 columns

## CSV Format

```csv
Name,Feature1,Feature2,Feature3,Feature4
Item1,10,20,30,40
Item2,15,25,35,45
Item3,12,22,32,42
```

- First column: Identifier (any text)
- Remaining columns: Numeric values for criteria

## Project Structure

```
topsis-web-service/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html     # Web form interface
├── uploads/           # Temporary file storage
└── results/           # Generated result files
```

## Example

**Input:**
- File: data.csv
- Weights: 1,1,1,1,1
- Impacts: +,+,+,+,-
- Email: user@example.com

**Output:**
Email sent with CSV containing:
- Original data columns
- Topsis Score
- Rank

## License

MIT
