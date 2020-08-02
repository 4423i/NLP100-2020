import pandas as pd

csv_file = 'popular-names.txt'
csv_input = pd.read_csv(csv_file, sep='\t', header=None)
print(csv_input[0].unique())