import sys
import csv
import os.path
SharePrices = []
YearsMonths=[]
columns=[]
rownum=1

file_name=raw_input('Please enter csv file name:')
file_exist=os.path.isfile(file_name)
if not file_exist:
	print ":file: %s  not found "%(file_name)
	exit(1)
with open(file_name, 'r',) as f:
    	reader = csv.reader(f)	
    	for  line in reader:
        	if 1 < rownum:		#Skipping Header line
			yearmonth=line[0:2]  # get  time from each  line record
			YearsMonths.append(yearmonth) # store time record 
        		monthlyshareprice=line[2:] # get and store  monthly share price value from each line record
        		SharePrices.append(monthlyshareprice)
        		columnwisevalues = zip(*SharePrices)
		else:
			rownum+=1	#Skipped Header line
rownum+=1
f.close()
for index, col in  enumerate(columnwisevalues):
	col=map(float,col)
	maxvalue=max(col)
	print 'maxShareprice is:',maxvalue
	rowindex=col.index(maxvalue)
	maxpricemonth=YearsMonths[0:][rowindex]
	print "For company=%s max share price = %s found in  period %s"%(index,maxvalue,maxpricemonth)