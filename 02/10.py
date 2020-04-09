import csv
import pprint
import pandas as pd

with open('popular-names.txt') as f:
    reader = csv.reader(f)
    print(len([row for row in reader]))

#pandasを使う方法，こっちのほうが遅い．    
#df = pd.read_csv('popular-names.txt')
#print(len(df))