#!/usr/bin/python

import sys
import re


InFile = open(sys.argv[1])

result = []
k = 0
for i in InFile:
	k = k + float(i)
	match = re.search('^0$',i)
	if match:
		result.append(i)

l = len(result)

sys.stdout.write(sys.argv[1] + '\n' + str(l/float(300))+ '\n' + str(k/float(300))+'\n') #file path, % of recovered trees and average number of columns removed

