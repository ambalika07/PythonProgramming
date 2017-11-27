# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import csv


path = "C:/Users/ambalika/Desktop/Python/federalist_papers/"

os.mkdir( path, 755 );

print("Path is created")      

essay_num = 0
fileName =''
with open('C:/Users/ambalika/Desktop/Python/1401.txt','r') as f:
	for line in f:
		if "FEDERALIST No." in line:
			if essay_num != 0:
				f1.close()
			essay_num+=1
			fileName = 'federalist_no_'+str(essay_num)+'.txt'
			f1= open(path + fileName,'w')	
		
		if essay_num>0:
			f1.writelines(line)
f1.writelines(line)
f1.close()
