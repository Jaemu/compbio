from bx.intervals.io import GenomicIntervalReader
from bx.bbi.bigwig_file import BigWigFile
import numpy as np
import matplotlib.pyplot as plt
from pygr import sqlgraph
import math as math
import time
import pickle

annotations = open('/Users/JME/Documents/CSE549/hg19.txt', 'r')
peakdata = open('/Users/JME/Documents/CSE549/pol2.narrowPeak', 'r')
chroms = pickle.load(open('/Users/JME/Documents/CSE549/chrom_data.p', 'rb'))

peaks = {}
for i in chroms.keys():
	peaks[i] = {}

for line in peakdata:
	p = line.split('\t')
	if p[0] in chroms:
		chrm = chroms[p[0]]
		for gene in chroms[p[0]].keys():
			print(gene)
			if int(gene) <= int(p[1]):
				if int(p[2]) <= int(chrm[gene][0]):
					print('Gene start: ' + str(gene) + ", end: " + str(chrm[gene][0]) + ", peak start: " + p[1] + ", peak end: " + str(p[2]))
					peaks[p[0]][gene] = {}
					peaks[p[0]][gene][p[1]] = p

print(peaks)
pickle.dump(peaks, open('peak_data.p', 'wb'))