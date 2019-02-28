#create full files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import shutil
import os.path
import subprocess

inputdir = '/Users/schulte/xfitter/F2_Analysis/Analysis/29_08_2018_10P/'

for name in os.listdir(inputdir):

	if name == '.DS_Store':
		continue
	
	direct = inputdir + name
	print('I am doing:')
	print(direct)
	
	os.chdir(direct)
	
	print('xfitter is running')
	py2output = subprocess.check_output("xfitter", shell=True)

	
	
	
	End = py2output[-24:]
	print(End)
	if End.rstrip() == 'End of Message Summary':
		print('End of xfitter')
		py2output2 = subprocess.check_output("xfitter-draw --root output", shell=True)
		print('Plots are produced')
		End_draw = py2output2[-34:]

		if End.rstrip() == 'Plots saved in: output/plots.pdf':
			print('End of drawing')
			continue






print('I am done!!!')
