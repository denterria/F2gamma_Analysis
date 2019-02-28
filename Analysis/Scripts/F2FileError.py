#create full files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import shutil
import math







file_list = [f for f in os.listdir('/Users/schulte/F2_Analysis/TestData/') if os.path.isfile(os.path.join('/Users/schulte/F2_Analysis/TestData/', f))]
print file_list


Prozent = 1.1
OutputFolder = '/Users/schulte/F2_Analysis/Error/'










for fi in file_list:
	print(fi)
	
	if fi == ".DS_Store":
		continue

	infile = open('/Users/schulte/F2_Analysis/Data/'+fi, 'r') 
	a,b = fi.split('.')
	
	
	c,d,e = a.split('_')
	
	Q02 = d +'.'+ e
	print('Q02 = %s' % Q02)
	
	
	#Get Q02 value
	
	
	
	directory = OutputFolder 
	if not os.path.exists(directory):
		os.makedirs(directory)
		
	out = directory + fi
	outfile = open(out, 'w')
	

	
	
	
	

			
			

		
		
		
		
	 
	counter = False
	End_header = 0;

	for line in infile:
		
		print line
		End_header = End_header + 1
		print(End_header)
		line2 = line.rstrip()
		
		if line2 == '  NColumn =   6':
			outfile.write('  NColumn =   4\n')
			continue
		if line2 == '  ColumnName = "Q2","x","Sigma", "stat","sys","sys"':
			outfile.write('  ColumnName = "Q2","x","Sigma", "stat"\n')
			continue
		if line2 == '  ColumnType = 2*"Bin","Sigma", 3*"Error"':
			outfile.write('  ColumnType = 2*"Bin","Sigma", 1*"Error"\n')
			continue
		if line2 == '  Percent = 3*false':
			outfile.write('  Percent = 1*false"\n')
			continue
		elif line2 != '  ColumnType = 2*"Bin","Sigma", 3*"Error"':
			if line2 != '  NColumn =   6':
				if line2 != '  ColumnType = 2*"Bin","Sigma", 3*"Error"':
					if line2 != '  Percent = 3*false':
						outfile.write(line)
		
		

		if line2 == "&PlotDesc": 
			counter = True

		if counter == True:
			if line2 == "&End": 
				break

	table_file = '/Users/schulte/F2_Analysis/Data/'+fi
	print(table_file)
	table = pd.read_fwf(table_file,skiprows=(End_header), sep='\t', engine='python', dtype='float')
	

	
	data1 = table['Unnamed: 3']
	data2 = table['Unnamed: 4']
	
	data3 = data1*data1
	data4 = data2*data2
	data5 = data3 + data4
	data6 =np.sqrt(data5)
	table['Unnamed: 3']=data6
	del table['Unnamed: 4']
	del table['Unnamed: 5']

	print data2
	table.to_csv(outfile,header=None,index=False, sep='\t',float_format='%g')

