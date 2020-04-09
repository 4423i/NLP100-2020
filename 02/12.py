import re
import csv
#import pprint
#import pandas as pd

with open('col1.txt', 'w') as c1:
    with open('col2.txt', 'w') as c2:
        with open('popular-names.txt') as f:
            reader = csv.reader(f,delimiter='\t')
            for row in reader:
                print(row)
                c1.write(row[0]+"\n")
                c2.write(row[1]+"\n")