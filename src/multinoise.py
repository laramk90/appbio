#!/usr/bin/python

import sys
import re
from Bio import AlignIO
from noise import *

for i in range(1,len(sys.argv)):
	k,align,l,m = noise(sys.argv[i])
	
for record in align:
	out = ''
	for i in k:
		out += str(record.seq[i])
	sys.stdout.write(out+'\n')
	
if len(k) > 0:	
	sys.stderr.write(str(l)+' columns were removed from this alignment\n')
elif len(m) == 0:
	sys.stderr.write('Error: Empty file\n')
elif len(k) == 0:
	sys.stderr.write('All columns were removed from this alignment\n')



