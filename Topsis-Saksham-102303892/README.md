# topsis-saksham-102303892


## Description

topsis-saksham-102303892 is a Python library for dealing with Multiple Criteria Decision Making(MCDM) problems by using Technique for Order of Preference by Similarity to Ideal Solution(TOPSIS).

## Installation

Use the package manager pip to install topsis-saksham-102303892.

```bash
pip install topsis-saksham-102303892
```

## Usage

Enter csv filename followed by .csv extension, then enter the weights vector with vector values separated by commas, followed by the impacts vector with comma separated signs (+,-)

```bash
topsis sample.csv "1,1,1,1" "+,-,+,+"
```

or vectors can be entered without " "

```bash
topsis sample.csv 1,1,1,1 +,-,+,+
```

But the second representation does not provide for inadvertent spaces between vector values. So, if the input string contains spaces, make sure to enclose it between double quotes (" ").

To view usage help, use:

```bash
topsis /h
```

## Example

### sample.csv

A csv file showing data for different mobile handsets having varying features.

| Model | Storage space(in gb) | Camera(in MP) | Price(in $) | Looks(out of 5) |
|-------|---------------------|---------------|-------------|----------------|
| M1    | 16                  | 12            | 250         | 5              |
| M2    | 16                  | 8             | 200         | 3              |
| M3    | 32                  | 16            | 300         | 4              |
| M4    | 32                  | 8             | 275         | 4              |
| M5    | 16                  | 16            | 225         | 2              |

weights vector = [ 0.25 , 0.25 , 0.25 , 0.25 ]

impacts vector = [ + , + , - , + ]

### Input:

```bash
topsis sample.csv "0.25,0.25,0.25,0.25" "+,+,-,+"
```

### Output:

```
      TOPSIS RESULTS
-----------------------------

    P-Score  Rank
1  0.534277     3
2  0.308368     5
3  0.691632     1
4  0.534737     2
5  0.401046     4
```

The output is also saved to a file named `output-result.csv`.

## Other Notes

- The first column and first row are removed by the library before processing, in attempt to remove indices and headers. So make sure the csv follows the format as shown in sample.csv.
- Make sure the csv does not contain categorical values.
- Input file must have at least 3 columns.
- All columns except the first must contain numeric values only.
- Number of weights must equal the number of criteria (columns - 1).
- Number of impacts must equal the number of criteria.
- Impacts must be either + or -.

## License

MIT
