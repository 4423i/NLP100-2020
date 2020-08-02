import csv
from operator import itemgetter
file = open('popular-names.txt','r')
data = []
for a,b,c,d in csv.reader(file,delimiter="\t"):
    data.append((a,b,int(c),d))

data.sort(key = itemgetter(2),reverse=True)
for i in data:
    print(*i)

#こっちのほうが遅い
#import pandas as pd
#
#data = pd.read_csv('popular-names.txt', sep='\t', header=None)
#print(data.sort_values(2, ascending=False))