import csv,collections
file = open('popular-names.txt','r')
data = []
for a,b,c,d in csv.reader(file,delimiter="\t"):
    data.append(a)

freq = collections.Counter(data).most_common()
for name,count in freq:
    print(name,count)