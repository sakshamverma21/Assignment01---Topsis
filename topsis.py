import sys
import pandas as pd
import numpy as np
import os

def error(msg):
    print("Error:", msg)
    sys.exit(1)

def main():
    # ---------- Check parameter count ----------
    if len(sys.argv) != 5:
        error("Usage: python topsis.py <InputFile> <Weights> <Impacts> <OutputFile>")

    input_file = sys.argv[1]
    weights = sys.argv[2]
    impacts = sys.argv[3]
    output_file = sys.argv[4]

    # ---------- File not found ----------
    if not os.path.exists(input_file):
        error("Input file not found")

    # ---------- Read CSV ----------
    try:
        df = pd.read_csv(input_file)
    except:
        error("Unable to read input file")

    # ---------- Check columns ----------
    if df.shape[1] < 3:
        error("Input file must contain three or more columns")

    data = df.iloc[:, 1:]

    # ---------- Check numeric ----------
    for col in data.columns:
        if not pd.api.types.is_numeric_dtype(data[col]):
            error("All columns from 2nd to last must be numeric")

    # ---------- Parse weights & impacts ----------
    try:
        weights = list(map(float, weights.split(",")))
        impacts = impacts.split(",")
    except:
        error("Weights and impacts must be separated by commas")

    n_cols = data.shape[1]

    if len(weights) != n_cols or len(impacts) != n_cols:
        error("Number of weights, impacts, and columns must be same")

    # ---------- Check impacts ----------
    for i in impacts:
        if i not in ['+', '-']:
            error("Impacts must be either + or -")

    # ---------- Step 1 Normalize ----------
    norm_data = data.copy()
    for col in data.columns:
        norm_data[col] = data[col] / np.sqrt((data[col]**2).sum())

    # ---------- Step 2 Weighted ----------
    weighted = norm_data.copy()
    for i in range(n_cols):
        weighted.iloc[:, i] = weighted.iloc[:, i] * weights[i]

    # ---------- Step 3 Ideal best & worst ----------
    ideal_best = []
    ideal_worst = []

    for i in range(n_cols):
        col = weighted.iloc[:, i]
        if impacts[i] == '+':
            ideal_best.append(col.max())
            ideal_worst.append(col.min())
        else:
            ideal_best.append(col.min())
            ideal_worst.append(col.max())

    ideal_best = np.array(ideal_best)
    ideal_worst = np.array(ideal_worst)

    # ---------- Step 4 Distance ----------
    dist_best = np.sqrt(((weighted - ideal_best) ** 2).sum(axis=1))
    dist_worst = np.sqrt(((weighted - ideal_worst) ** 2).sum(axis=1))

    # ---------- Step 5 Score ----------
    score = dist_worst / (dist_best + dist_worst)

    df["Topsis Score"] = score

    # ---------- Ranking ----------
    df["Rank"] = df["Topsis Score"].rank(ascending=False, method='dense').astype(int)

    # ---------- Save ----------
    df.to_csv(output_file, index=False)

    print("TOPSIS completed successfully!")
    print("Output saved to:", output_file)


if __name__ == "__main__":
    main()
