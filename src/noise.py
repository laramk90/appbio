#!/usr/bin/python

from Bio import AlignIO
import re
import sys

def noise(x):
	align = AlignIO.read(x,"fasta") 

	#check column for column if it should be considered noisy 

	noisy = []
	for i in range (0,len(align[0])):
		column = str(align[:,i])
		total = float(len(align))
		indel = column.count('-') #number of indels in each column i
		uniq = list(set(column)) #unique list of the amino acids in each column i
		sum = 0
		if indel is not None: 
			if indel/total > 0.5:
				noisy.append(i)
			elif len(uniq)/total >= 0.5:
				noisy.append(i)

	m = range(0,len(align[0]))
	k = list(set(m)-set(noisy))

	
	return k,align,len(noisy),m
	
	

