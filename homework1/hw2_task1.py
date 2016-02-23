import pandas as pd
import seaborn as sns
import csv
import dateutil
import csv
import sys

if __name__=='__main__':

	if len(sys.argv)<2:
	    sys.stderr.write('USAGE: python %s <INPUT_CSV>\n' % sys.argv[0])
	    sys.exit(1)
	    
	with open(sys.argv[1], 'r') as fi:
	    reader = csv.DictReader(fi)
	    for row in first_ride(reader):
	        print ','.join(map(row.get, reader.fieldnames))

	count = {}

	for i in reader:
	    count[i] = count.get(i,0) + 1  

	df = pd.DataFrame.from_dict(count, 'index')

	total = df[0].sum()
	curSum = 0
	median = None

	for k,v in sorted(count.iteritems()):
	    curSum += v
	    if curSum>=total/2.0:
	        median = k
	        break

	sys.stdout.write(median)
	sys.exit(0)