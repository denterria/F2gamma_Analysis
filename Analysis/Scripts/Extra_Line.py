#create full files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import shutil



Inputpath = '/Users/schulte/xfitter/F2_Analysis/Analysis/Test/'



file_list = [f for f in os.listdir(Inputpath) if os.path.isfile(os.path.join(Inputpath, f))]
print file_list


Prozent = 1.0
OutputFolder = Inputpath



















for fi in file_list:
	print(fi)
	
	if fi == ".DS_Store":
		continue

	infile = open(Inputpath + fi, 'r+') 
	a,b = fi.split('.')
	
	
	c,d,e = a.split('_')
	
	Q02 = d +'.'+ e
	print('Q02 = %s' % Q02)
	
	
	#Get Q02 value
	

	


	counter = False
	End_header = 0
	
	print "header end"


	for line in infile:
		infile.write(line)
		line = line.rstrip()
		End_header = End_header + 1
		if line == "&PlotDesc": 
			counter = True

		if counter == True:
			if line == "&End": 
				infile.write('Hello World')
				continue


