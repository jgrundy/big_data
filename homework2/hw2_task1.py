#Jonathan Grundy (jdg526)
import pandas as pd
import csv
import sys

#import data from shell
if len(sys.argv)<2:
    sys.stderr.write('USAGE: python %s <INPUT_CSV>\n' % sys.argv[0])
    sys.exit(1)

#function to import and parse DictReader and return age
def citibike_hod(filename):
    with open(filename, 'r') as fi:
        reader = csv.DictReader(fi)
        for row in reader:
            if row['birth_year'] != '': 
            	age = 2016 - int(row['birth_year'])
            	yield age

#load data into dictionary by age
count = {}
g = citibike_hod(sys.argv[1])
for hod in g:
    count[hod] = count.get(hod, 0) + 1 #key=age, value=count
df = pd.DataFrame.from_dict(count, 'index')

#calculate median
total = df[0].sum()
curSum = 0
median = None
for k,v in sorted(count.iteritems()):
    curSum += v
    if curSum>=total/2.0:
        median = k
        break

#return value to shell
print median