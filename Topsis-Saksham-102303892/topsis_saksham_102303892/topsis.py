import sys
import pandas as pd
import numpy as np
import os

def topsis():
    # Check for help command
    if len(sys.argv) == 2 and sys.argv[1] in ['/h', '-h', '--help', 'help']:
        print("\nTOPSIS - Technique for Order of Preference by Similarity to Ideal Solution")
        print("="*70)
        print("\nUsage: topsis <InputFile> <Weights> <Impacts>")
        print("\nArguments:")
        print("  InputFile : CSV file containing the data")
        print("  Weights   : Comma-separated weights for each criterion")
        print("  Impacts   : Comma-separated impacts (+ or -) for each criterion")
        print("\nExample:")
        print('  topsis sample.csv "0.25,0.25,0.25,0.25" "+,+,-,+"')
        print("  topsis sample.csv 0.25,0.25,0.25,0.25 +,+,-,+")
        print("\nOutput: Results are displayed and saved to 'output-result.csv'\n")
        sys.exit(0)

    if len(sys.argv) != 4:
        print("Error: Incorrect number of arguments")
        print("Usage: topsis <InputFile> <Weights> <Impacts>")
        print("For help, use: topsis /h")
        sys.exit(1)

    input_file = sys.argv[1]
    weights = sys.argv[2]
    impacts = sys.argv[3]

    if not os.path.exists(input_file):
        print("Error: File not found")
        sys.exit(1)

    df = pd.read_csv(input_file)

    if df.shape[1] < 3:
        print("Error: File must contain at least 3 columns")
        sys.exit(1)

    data = df.iloc[:,1:]

    for col in data.columns:
        if not pd.api.types.is_numeric_dtype(data[col]):
            print("Error: Non numeric values found")
            sys.exit(1)

    weights = list(map(float, weights.split(",")))
    impacts = impacts.split(",")

    if len(weights) != data.shape[1]:
        print(f"Error: Number of weights ({len(weights)}) does not match number of criteria ({data.shape[1]})")
        sys.exit(1)

    if len(impacts) != data.shape[1]:
        print(f"Error: Number of impacts ({len(impacts)}) does not match number of criteria ({data.shape[1]})")
        sys.exit(1)

    for i in impacts:
        if i not in ['+','-']:
            print("Error: Impacts must be + or -")
            sys.exit(1)

    # Normalize
    norm = data / np.sqrt((data**2).sum())

    # Weight
    for i in range(len(weights)):
        norm.iloc[:,i] *= weights[i]

    ideal_best = []
    ideal_worst = []

    for i in range(len(weights)):
        col = norm.iloc[:,i]
        if impacts[i] == '+':
            ideal_best.append(col.max())
            ideal_worst.append(col.min())
        else:
            ideal_best.append(col.min())
            ideal_worst.append(col.max())

    dist_best = np.sqrt(((norm - ideal_best)**2).sum(axis=1))
    dist_worst = np.sqrt(((norm - ideal_worst)**2).sum(axis=1))

    score = dist_worst/(dist_best+dist_worst)

    result = pd.DataFrame({
        "P-Score": score,
        "Rank": score.rank(ascending=False).astype(int)
    }, index=range(1, len(score)+1))

    print("\n      TOPSIS RESULTS")
    print("-----------------------------\n")
    print(result)

    # Save result to output file
    output_df = df.copy()
    output_df['Topsis Score'] = score.values
    output_df['Rank'] = result['Rank'].values
    output_df.to_csv('output-result.csv', index=False)
    print("\nResults saved to 'output-result.csv'")


if __name__ == "__main__":
    topsis()
