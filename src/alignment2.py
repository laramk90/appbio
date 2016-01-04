#!/usr/bin/python

from Bio import AlignIO
from collections import Counter
import re
import sys

align = AlignIO.read(sys.argv[1],"fasta")

noisy = []

for i in range(0,len(align[0])):
    column = str(align[:,i])
    total = float(len(align))
    # Determining whether the column is noisy or not
    # Condition 1 : there are more than 50% indels
    g = column.count('-')
    if g is not None:
        if g/total >= 0.5:
            noisy.append(i)
    # Condition 2 : at least 50% unique amino acids
    noindels = re.sub('[-]','',column)
    uniques = [k for k, v in Counter(noindels).iteritems() if v == 1]
    if len(uniques)/float(len(noindels)) >= 0.5:
        noisy.append(i)
    # Condition 3 : no amino acid appears more than twice
    twice = [k for k, v in Counter(noindels).iteritems() if v > 2]
    if twice is None:
        noisy.append(i)
    

k = range(0,len(align[0]))
k = list(set(k)-set(noisy))
l = len(noisy)
m = range(0,len(align[0]))


if len(k) > 0:	#show how many columns are removed from the alignment
	sys.stderr.write(str(l)+' columns were removed from this alignment\n')
elif len(m) == 0: #error message when there is no record in the given alignment file
	sys.stderr.write('Error: Empty file\n')
elif len(k) == 0: #return a message if all columns are removed
	sys.stderr.write('All columns were removed from this alignment\n')

for record in align:
    out = ''
    for i in k:
        out += str(record.seq[i])
    print '>' + record.id
    g = []
    for i in range(0,len(out),60):
        z = out[i:i+60]
        g.append(z)
    for n in g:
        print n