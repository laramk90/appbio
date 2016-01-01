#!/usr/bin/python

from Bio import AlignIO
import re
import sys 

align = AlignIO.read(sys.argv[1],'fasta')

def cut_a_gap():
    n = float(len(align[0]))
    i = 0
    while i < n:
        if align[:, i].count('-') / n > 0.5:
            if i == 0:
                align = align[:, 1:]
            elif i+1 == n:
                align = align[:, :i]
            else:
                align = align[:, :i] + align[:, i+1:]
            n -= 1  #  seq. 1 shorter
        else:  #  nothing to delete, proceed
            i += 1
	sys.stdout.write(align[:,i])