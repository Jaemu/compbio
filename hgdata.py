from bx.intervals.io import GenomicIntervalReader
from bx.bbi.bigwig_file import BigWigFile
import numpy as np
import matplotlib.pyplot as plt
from pygr import sqlgraph
import math as math
import time
import pickle

trScores = {}
maxScore = 0
maxGene = ''
chroms = {}

for i in xrange(1, 24):
	chroms['chr' + str(i)] = {}


pol2 = BigWigFile(open('/Users/JME/Documents/CSE549/hg19.bigWig'))
annotations = open('/Users/JME/Documents/CSE549/hg19.txt', 'r')
for line in annotations:
	lines = line.split('\t')
	if(lines[1] in chroms.keys()):
		chroms[lines[1]][int(lines[3])] = [int(lines[4]), lines[2]]

for i in chroms.keys():
	for j in chroms[i]:
		if not j in trScores.keys():
			start = 0
			end = 0
			if chroms[i][j][1] == '-':
				start = chroms[i][j][0]
				end = j
			else:
				start = j
				end = chroms[i][j][0]
			startTr = pol2.query(i, start - 30, start + 300, 1)
			endTr = pol2.query(i, start + 301, end, 1)
			if startTr and endTr:
				if startTr[0]['mean'] > 0 and endTr[0]['mean'] > 0:
					trScores[j] = 0
					trScores[j] = (startTr[0]['mean'])/ (endTr[0]['mean'])	
					if trScores[j] > maxScore:
						maxScore = trScores[j]
						maxGene = j

pickle.dump(chroms, open('chrom_data.p', 'wb'))
pickle.dump(trScores, open('scores.p', 'wb'))
print("Max: " + maxScore  + ", gene: " + maxGene)