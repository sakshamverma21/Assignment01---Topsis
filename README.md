# Assignment 01 - TOPSIS Implementation

**Submitted by:** Saksham Verma | **Roll No:** 102303892 | **Course:** UCS633 - Predictive Analytics

---

## 1. Methodology

TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) is a multi-criteria decision-making method that ranks alternatives based on their proximity to the ideal solution.

**Algorithm Steps:**
1. **Normalize** the decision matrix using vector normalization
2. **Apply weights** to normalized values
3. **Identify ideal best** (V⁺) and **ideal worst** (V⁻) solutions
4. **Calculate Euclidean distances** from ideal solutions
5. **Compute TOPSIS score** and rank alternatives

The alternative closest to the ideal solution and farthest from the negative-ideal solution is ranked highest.

---

## 2. Description

This assignment implements TOPSIS in three formats:

### Part I: Command-Line Tool
Python script with comprehensive validation and error handling.
```bash
python topsis.py data.csv "1,1,1,1,1" "+,+,+,+,-" result.csv
```

### Part II: PyPI Package
Published Python package for easy installation and reuse.
```bash
pip install topsis-saksham-102303892
topsis data.csv "1,1,1,1,1" "+,+,+,+,-"
```

### Part III: Web Service
Flask-based web application with:
- File upload interface
- Weights and impacts input
- Email result delivery
- Input validation (weights count = impacts count, + or - symbols only)

---

## 3. Input / Output

### Input CSV Format
```csv
Fund Name,P1,P2,P3,P4,P5
M1,0.84,0.71,5.7,62.9,17.54
M2,0.89,0.79,5.2,54.5,15.35
M3,0.93,0.86,5.7,52.1,14.9
```
- First column: Identifier
- Remaining columns: Numeric criteria values
- Minimum 3 columns required

### Output CSV Format
```csv
Fund Name,P1,P2,P3,P4,P5,Topsis Score,Rank
M1,0.84,0.71,5.7,62.9,17.54,0.6816,3
M2,0.89,0.79,5.2,54.5,15.35,0.7488,2
M3,0.93,0.86,5.7,52.1,14.9,0.4232,5
```
- Adds **Topsis Score** (0-1 scale)
- Adds **Rank** (1 = best alternative)

---

## 4. Live Links

**PyPI Package:** https://pypi.org/project/topsis-saksham-102303892/

**GitHub Repository:** https://github.com/sakshamverma21/Assignment01---Topsis

**Web Service:** (Local deployment - `python app.py` in topsis-web-service/)

---

## 5. Screenshot of the Interface

### Web Service Interface
![TOPSIS Web Interface](screenshot.png)

**Features:**
- Clean and intuitive form design
- File upload for CSV input
- Text inputs for weights and impacts
- Email field for result delivery
- Orange submit button with validation
- Success/error message display

---

## Repository Structure

---

## Repository Structure

```
Assignment01---Topsis/
├── README.md
├── topsis.py                    # Part I: CLI script
├── data.csv                     # Sample input
├── output-result.csv            # Sample output
├── Topsis-Saksham-102303892/   # Part II: PyPI package
└── topsis-web-service/          # Part III: Web application
    ├── app.py
    ├── templates/index.html
    ├── requirements.txt
    └── .env.example
```

---

**License:** MIT

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


