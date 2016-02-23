#Jonathan Grundy (jdg526)

import pandas as pd
import csv
import dateutil
import sys

def first_ride(reader):
    counter = 01
    for row in reader:
    	startDay = dateutil.parser.parse(row['starttime'])
    	if startDay.day == counter:
			counter = counter + 1
			yield row

if len(sys.argv)<2:
    sys.stderr.write('USAGE: python %s <INPUT_CSV>\n' % sys.argv[0])
    sys.exit(1)

with open(sys.argv[1], 'r') as fi:
    reader = csv.DictReader(fi)
    for row in first_ride(reader):
        print ','.join(map(row.get, reader.fieldnames))
        print