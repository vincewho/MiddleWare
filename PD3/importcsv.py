#This will import the csv file that is provided into a dictionary list.

import csv
import sys
from collections import defaultdict

def createDict(csv_file):
	lab_dict = defaultdict(list)

	filein=open(csv_file, 'r')
	data=csv.DictReader(filein, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True)

	return data

csv_file = 'test_results.csv'
data = createDict(csv_file)
csv_dict_list = [row for row in data]

#To see the list, uncomment the line below:
#print csv_dict_list
