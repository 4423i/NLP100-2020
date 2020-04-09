import pandas as pd

csv_file = 'popular-names.txt'
csv_input = pd.read_csv(csv_file, sep = "\t")

print(csv_input.head(int(input()) - 1))