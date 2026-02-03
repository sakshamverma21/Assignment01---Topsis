# Assignment 01 - TOPSIS Implementation and Deployment

This assignment implements TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) for Multi-Criteria Decision Making (MCDM) problems in three different formats: command-line tool, Python package, and web service.

---

## 📋 Assignment Overview

### Part I: Command-Line Implementation
A Python script that performs TOPSIS analysis via command line with comprehensive input validation and error handling.

### Part II: PyPI Package
A published Python package available on PyPI for easy installation and use across projects.

**Package Link:** [topsis-saksham-102303892](https://pypi.org/project/topsis-saksham-102303892/)

### Part III: Web Service
A Flask-based web application that accepts file uploads and sends analysis results via email.

---

## 1. TOPSIS Methodology

TOPSIS is a multi-criteria decision analysis method that identifies the alternative closest to the ideal solution and farthest from the negative-ideal solution.

### Algorithm Steps:

1. **Normalization**: Convert the decision matrix to normalized form using vector normalization
   ```
   r_ij = x_ij / √(Σ x_ij²)
   ```

2. **Weighted Normalization**: Multiply normalized values by their respective weights
   ```
   v_ij = w_j × r_ij
   ```

3. **Ideal Solutions**: Determine ideal best (V⁺) and ideal worst (V⁻) values
   - For benefit criteria (+): V⁺ = max, V⁻ = min
   - For cost criteria (-): V⁺ = min, V⁻ = max

4. **Distance Calculation**: Calculate Euclidean distances from ideal solutions
   ```
   S⁺ = √(Σ(v_ij - v_j⁺)²)
   S⁻ = √(Σ(v_ij - v_j⁻)²)
   ```

5. **TOPSIS Score**: Calculate performance score and rank alternatives
   ```
   P = S⁻ / (S⁺ + S⁻)
   ```

---

## 2. Implementation Details

### Part I: Command-Line Tool

**File:** `topsis.py`

**Usage:**
```bash
python topsis.py <InputFile> <Weights> <Impacts> <ResultFile>
```

**Example:**
```bash
python topsis.py data.csv "1,1,1,1,1" "+,+,+,+,-" output-result.csv
```

**Validation Checks:**
- ✅ Correct number of parameters
- ✅ File existence verification
- ✅ Minimum 3 columns requirement
- ✅ Numeric value validation (columns 2 onwards)
- ✅ Equal count of weights, impacts, and criteria
- ✅ Impact symbols validation (+ or -)
- ✅ Comma-separated format enforcement

---

### Part II: PyPI Package

**Package Name:** `topsis-saksham-102303892`

**Installation:**
```bash
pip install topsis-saksham-102303892
```

**Usage:**
```bash
topsis data.csv "1,1,1,1,1" "+,+,+,+,-"
```

**Help Command:**
```bash
topsis /h
```

**Package Structure:**
```
Topsis-Saksham-102303892/
├── topsis_saksham_102303892/
│   ├── __init__.py
│   └── topsis.py
├── setup.py
├── pyproject.toml
├── README.md
├── LICENSE
└── MANIFEST.in
```

**Features:**
- Command-line interface via entry points
- Automatic output file generation
- Comprehensive error messages
- Complete documentation

---

### Part III: Web Service

**Technology Stack:** Flask, Python, SMTP

**Features:**
- 📁 File upload interface
- ⚖️ Weights and impacts input
- 📧 Email result delivery
- ✅ Input validation
- 🎨 Clean, responsive UI

**Setup:**
```bash
cd topsis-web-service
pip install -r requirements.txt
python app.py
```

**Access:** http://127.0.0.1:5000

**Validation Rules:**
- Number of weights = Number of impacts
- Impacts must be + or -
- Valid email format required
- CSV must contain numeric values

---

## 3. Input/Output Format

### Input CSV Structure
```csv
Name,Criterion1,Criterion2,Criterion3,Criterion4
Item1,10,20,30,40
Item2,15,25,35,45
Item3,12,22,32,42
```

**Requirements:**
- First column: Identifier (any type)
- Remaining columns: Numeric values only
- Minimum 3 columns total

### Output CSV Structure
```csv
Name,Criterion1,Criterion2,Criterion3,Criterion4,Topsis Score,Rank
Item1,10,20,30,40,0.534277,3
Item2,15,25,35,45,0.691632,1
Item3,12,22,32,42,0.401046,2
```

**Added Columns:**
- **Topsis Score**: Performance score (0 to 1)
- **Rank**: Ranking based on score (1 = best)

---

## 4. Sample Execution

### Command-Line Example

**Input Command:**
```bash
python topsis.py data.csv "1,1,1,1,1" "+,+,+,+,-" result.csv
```

**Sample Input (data.csv):**
```csv
Fund Name,P1,P2,P3,P4,P5
M1,0.84,0.71,5.7,62.9,17.54
M2,0.89,0.79,5.2,54.5,15.35
M3,0.93,0.86,5.7,52.1,14.9
```

**Sample Output (result.csv):**
```csv
Fund Name,P1,P2,P3,P4,P5,Topsis Score,Rank
M1,0.84,0.71,5.7,62.9,17.54,0.681556,3
M2,0.89,0.79,5.2,54.5,15.35,0.748839,2
M3,0.93,0.86,5.7,52.1,14.9,0.423169,5
```

---

## 5. Error Handling

### Common Errors and Messages

| Error Type | Message |
|-----------|---------|
| Missing parameters | "Usage: topsis <InputFile> <Weights> <Impacts> <ResultFile>" |
| File not found | "Error: File not found" |
| Insufficient columns | "Error: File must contain at least 3 columns" |
| Non-numeric values | "Error: Non-numeric values found" |
| Count mismatch | "Error: Number of weights (X) does not match number of criteria (Y)" |
| Invalid impacts | "Error: Impacts must be + or -" |
| Invalid email | "Invalid email format" |

---

## 6. Repository Structure

```
Assignment01---Topsis/
├── README.md                          # This file
├── topsis.py                          # Part I: Command-line script
├── data.csv                           # Sample input data
├── output-result.csv                  # Sample output
├── Topsis-Saksham-102303892/         # Part II: PyPI package
│   ├── topsis_saksham_102303892/
│   │   ├── __init__.py
│   │   └── topsis.py
│   ├── setup.py
│   ├── pyproject.toml
│   ├── README.md
│   ├── LICENSE
│   └── MANIFEST.in
└── topsis-web-service/                # Part III: Web application
    ├── app.py
    ├── templates/
    │   └── index.html
    ├── requirements.txt
    ├── .env.example
    ├── .gitignore
    └── README.md
```

---

## 7. Installation & Usage

### Part I: Direct Script
```bash
python topsis.py data.csv "1,1,1,1,1" "+,+,+,+,-" result.csv
```

### Part II: PyPI Package
```bash
pip install topsis-saksham-102303892
topsis data.csv "1,1,1,1,1" "+,+,+,+,-"
```

### Part III: Web Service
```bash
cd topsis-web-service
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your email credentials
python app.py
```

---

## 8. Key Features

### Comprehensive Validation
- Parameter count verification
- File existence checks
- Data type validation
- Dimensional consistency checks
- Format validation (email, impacts)

### User-Friendly Output
- Clear error messages
- Help documentation
- Result visualization
- Email delivery option

### Production-Ready
- Environment variable configuration
- Secure credential handling
- .gitignore for sensitive data
- Complete documentation

---

## 9. Testing Results

### Test Case 1: Valid Input
```bash
Input: data.csv with 5 criteria, weights="1,1,1,1,1", impacts="+,+,+,+,-"
Output: ✅ Success - Results generated with scores and ranks
```

### Test Case 2: Invalid Weights Count
```bash
Input: 5 criteria but 4 weights
Output: ✅ Error message displayed correctly
```

### Test Case 3: PyPI Installation
```bash
Command: pip install topsis-saksham-102303892
Result: ✅ Package installed and command-line tool accessible
```

### Test Case 4: Web Service
```bash
Test: Upload file, enter weights/impacts, submit email
Result: ✅ Email received with result file attached
```

---

## 10. Conclusion

This assignment successfully implements TOPSIS methodology in three complementary formats:

1. **Command-Line Tool**: Provides direct, scriptable access for automation and batch processing
2. **PyPI Package**: Enables easy distribution and integration into other Python projects
3. **Web Service**: Offers user-friendly interface for non-technical users

All implementations include robust validation, comprehensive error handling, and clear documentation. The package is publicly available on PyPI and ready for production use.

**PyPI Package:** https://pypi.org/project/topsis-saksham-102303892/

**GitHub Repository:** https://github.com/sakshamverma21/Assignment01---Topsis

---

## 📝 License

MIT License - See LICENSE file for details

---


