from bx.intervals.io import GenomicIntervalReader
from bx.bbi.bigwig_file import BigWigFile
import numpy as np
import matplotlib.pyplot as plt
from pygr import sqlgraph
import math as math
import time
import pickle

start_time = time.time()

pol2 = BigWigFile(open('/Users/JME/Documents/CSE549/hg19.bigWig'))
#serverInfo = sqlgraph.DBServerInfo(host='genome-mysql.cse.ucsc.edu', user='genome')
#genes = sqlgraph.SQLTable('hg19.knownGene', serverInfo=serverInfo, primaryKey='name')

trScores = {}
maxScore = 0
maxGene = ''
chroms = {}

chroms = pickle.load(open('chrom_data.p', 'rb'))
trScores = pickle.load(open('scores.p', 'rb'))

histData = []
for i in trScores:
	histData.append(trScores[i])

values, base = np.histogram(histData, 300)
cumulative = np.cumsum(values)
plt.plot(base[:-1], cumulative)
x = np.linspace(0,1)
plt.fill(x, histData, 'r')
plt.title("Genome-wide Distribution of TR Scores (cumulative)")
plt.ylabel('# of genes')
plt.xlabel('TR Score')
plt.show()


for i in chroms.keys():
	chromTrScores = []
	for j in chroms[i]:
		if j in trScores.keys():
			chromTrScores.append(trScores[j])
	print(chromTrScores)
	if len(chromTrScores) > 0: 
		values, base = np.histogram(chromTrScores, 100)
		cumulative = np.cumsum(values)
		plt.plot(base[:-1], cumulative, label=i, cumulative=True)
plt.title("Cumulative Distribution of TR Scores by Genome")
plt.ylabel('# of genes')
plt.xlabel('TR Score')
plt.show()

print("Time: " + str(time.time() - start_time)) 

#for i in genes:
#	target_gene = genes[i]
#	chrom = target_gene.chrom
#
#	
#	if start and end:
#		if start[0]['mean'] > 0 and end[0]['mean'] > 0:
#			trScores[target_gene.name] = 0
#			trScores[target_gene.name] = (start[0]['mean'])/ (end[0]['mean'])
#			if trScores[target_gene.name] > maxScore:
#				maxScore = trScores[target_gene.name]
#				maxGene = target_gene.name
#			print("Gene, " + target_gene.name + ", chrom, " + chrom + ", start" + str(target_gene.txStart) + ", stop" + str(target_gene.txEnd) + "pol2, " + str(trScores[target_gene.name]))
#print("Highest TR Value: " + maxScore)

