# TOPSIS Implementation

**Submitted by:** Saksham Verma | **Roll No:** 102303892

---

## Methodology

TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) is a multi-criteria decision-making method.

**Steps:**
1. Normalize the decision matrix
2. Apply weights to normalized values
3. Determine ideal best and ideal worst solutions
4. Calculate Euclidean distances from ideal solutions
5. Calculate performance score: `P = S⁻ / (S⁺ + S⁻)`
6. Rank alternatives (higher score = better)

---

## Description

This project implements TOPSIS in three ways:

### Part I: Command-Line Script
```bash
python topsis.py data.csv "1,1,1,1,1" "+,+,+,+,-" result.csv
```

### Part II: Python Package (PyPI)
```bash
pip install topsis-saksham-102303892
topsis data.csv "1,1,1,1,1" "+,+,+,+,-"
```

### Part III: Web Application
- Upload CSV file
- Enter weights and impacts
- Receive results via email
- Run locally: `cd topsis-web-service && python app.py`

---

## Links

**PyPI Package:** https://pypi.org/project/topsis-saksham-102303892/

**GitHub Repository:** https://github.com/sakshamverma21/Assignment01---Topsis

---

## Input/Output

**Input:**
```csv
Fund,P1,P2,P3,P4,P5
M1,0.84,0.71,5.7,62.9,17.54
M2,0.89,0.79,5.2,54.5,15.35
```

**Output:**
```csv
Fund,P1,P2,P3,P4,P5,Topsis Score,Rank
M1,0.84,0.71,5.7,62.9,17.54,0.682,3
M2,0.89,0.79,5.2,54.5,15.35,0.749,2
```

---

## Features

- ✅ Input validation (parameters, file format, numeric values)
- ✅ Error handling with clear messages
- ✅ Multiple deployment options (CLI, package, web)
- ✅ Email delivery for web service

---

## License

MIT


