import csv
import pprint

with open('popular-names.txt') as f:
    reader = csv.reader(f)
    print(len([row for row in reader]))