#create full files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import shutil



Inputpath = '/Users/schulte/xfitter/F2_Analysis/Analysis/Orderd_Data_by_Q2/'



file_list = [f for f in os.listdir(Inputpath) if os.path.isfile(os.path.join(Inputpath, f))]
print file_list


Prozent = 1.1
OutputFolder = '/Users/schulte/xfitter/F2_Analysis/Analysis/29_08_2018_10P/'




def multi_Err(data):
	data_new = data*Prozent
	return float(data_new) 















for fi in file_list:
	print(fi)
	
	if fi == ".DS_Store":
		continue

	infile = open(Inputpath + fi, 'r') 
	a,b = fi.split('.')
	
	
	c,d,e = a.split('_')
	
	Q02 = d +'.'+ e
	print('Q02 = %s' % Q02)
	
	
	#Get Q02 value
	
	
	
	directory = OutputFolder + a  +'/'
	if not os.path.exists(directory):
		os.makedirs(directory)
		
	out = directory + fi
	outfile = open(out, 'w')
	
	shutil.copy2('/Users/schulte//xfitter/F2_Analysis/Analysis/Steering_Files/minuit.in.txt' , directory)
	shutil.copy2('/Users/schulte/xfitter/F2_Analysis/Analysis/Steering_Files/ewparam.txt' , directory)

	
	
	
	
	steeringfile = open('/Users/schulte/xfitter/F2_Analysis/Analysis/Steering_Files/steering.txt', 'r')
	steering = open(directory + 'steering.txt', 'w')

#Write steeringfile
	for line in steeringfile:
		line2 = line.rstrip()
		if (line2 != "Input"):
			if(line2 != "Q02"):
				steering.write(line) 
		if(line2 == "Input"): 
			Path = "InputFileNames(1) = '%s'" % fi
			steering.write(Path)
		elif line2 == "Q02":
			steering.write('Q02     = %s ! Evolution starting scale' % Q02)
			
			

		
		
		
		
	 
	counter = False
	End_header = 0
	
	print "header end"


	for line in infile:
		outfile.write(line)
		line = line.rstrip()
		End_header = End_header + 1
		if line == "&PlotDesc": 
			counter = True

		if counter == True:
			if line == "&End": 
				break
	print End_header

	table_file = Inputpath + fi
	print table_file
	table = pd.read_fwf(table_file,skiprows=(End_header), sep='\t', engine='python', dtype='float')
	
	table['Unnamed: 3'] = table['Unnamed: 3'].apply(multi_Err)
	print table
	table.to_csv(outfile,header=None,index=False, sep='\t',float_format='%g')

