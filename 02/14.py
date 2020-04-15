import sys
import pandas as pd

csv_file = 'popular-names.txt'
csv_input = pd.read_csv(csv_file, sep = "\t", header=None)

n = int(sys.argv[1])
#n = int(input())

print(csv_input.head(n))