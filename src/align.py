#!/usr/bin/python

from Bio import AlignIO
import re
import sys


align = AlignIO.read(sys.argv[1],"fasta") 
noisy = []
for i in range(0,len(align[0])):
    column = str(align[:,i])
    total = float(len(align))
    g = column.count('-') # percentage of indels
    if g is not None:
        if g/total > 0.5:
            noisy.append(i)
    if len(set(column))/total >= 0.6:
        print column

k = range(0,len(align[0]))

k = list(set(k)-set(noisy))

print len(noisy)
print k

for record in align:
    out = ''
    for i in k:
        out += str(record.seq[i])
    print out