#!/usr/bin/python

import sys
import dendropy
from dendropy.calculate import treecompare
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('reftree')
parser.add_argument('tree')
args = parser.parse_args()

InFile = open(args.reftree)
tree = ''

for line in InFile:
	tree = line
	
tns = dendropy.TaxonNamespace()
tree1 = dendropy.Tree.get(data=tree,schema='newick',taxon_namespace=tns) #reference tree

InFile =open(args.tree)
tree = ''

for line in InFile:
	tree = line

tree2 = dendropy.Tree.get(data=tree,schema='newick',taxon_namespace=tns) #original or noise reduced tree

print(treecompare.symmetric_difference(tree1,tree2))

