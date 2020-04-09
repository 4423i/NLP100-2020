import re
import csv
#import pprint
#import pandas as pd
col1,col2 = [],[]
with open('col1.txt', 'r') as c1:
    f = csv.reader(c1)
    for row in f:
        col1.append(row)

with open('col2.txt', 'r') as c2:
    f = csv.reader(c2)
    for row in f:
        col2.append(row)

with open('colmerge.txt', 'w') as f:
    for i in range(len(col1)):
        f.write(col1[i][0]+"    "+col2[i][0]+"\n")