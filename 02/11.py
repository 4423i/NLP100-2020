import re
#import csv
#import pprint
#import pandas as pd

with open('popular-names-tab-to-space.txt', 'w') as t:
    with open('popular-names.txt') as f:
        for row in f:
            t.write(re.sub(r'\t',' ', row))