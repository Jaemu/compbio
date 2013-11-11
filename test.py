from bx.intervals.io import GenomicIntervalReader
from bx.bbi.bigwig_file import BigWigFile
import numpy as np
import matplotlib.pyplot as plt
from pygr import sqlgraph
import math as math


#Import chip-seq data for Sr2 and pol II
pol2 = BigWigFile(open('/Users/JME/Documents/CSE549/hg19.bigWig'))
#pol2_ser2 = BigWigFile(open('/Users/nathanposlusny/Documents/CS_Masters/CompBio/SemesterProject/Data_Sets/GSM935608_hg19_wgEncodeSydhTfbsGm12878Pol2s2IggmusSig.bigWig'))
#mySummary = bw.query("chr1", 10000,10500, 1)
#myInterval = bw.get("chr1", 10000, 10500)
#myArrayInterval = bw.get_as_array("chr1", 10000, 10500)

#Get the most recent genome annotations
#gene = 'uc010kyl.4'  #GADP gene
serverInfo = sqlgraph.DBServerInfo(host='genome-mysql.cse.ucsc.edu', user='genome')
genes = sqlgraph.SQLTable('hg19.knownGene', serverInfo=serverInfo, primaryKey='name')
#target_gene = genes[gene]
trScores = {}
maxScore = 0
for i in genes:
	target_gene = genes[i]
	trScores[target_gene.name] = 0
	chrom = target_gene.chrom
	exons = target_gene.exonCount
	exonStarts = target_gene.exonStarts
	exonEnds = target_gene.exonEnds
	genelength = math.fabs(target_gene.txStart - target_gene.txEnd)
	#Get exon information
	exonStartP = exonStarts.split(',')
	exonEndsP = exonEnds.split(',')
	exonStartP.pop()
	exonEndsP.pop()

	#Convert exon strings to integers
	exonStartA = []
	exonEndsA = []
	exonStartA = np.asarray([int(i) for i in exonStartP])
	exonEndsA = np.asarray([int(i) for i in exonEndsP])

	#print 'Gene start:',target_gene.txStart
	#print 'Gene end:',target_gene.txEnd
	#print 'Gene length: ', genelength
	#print 'Exon starts: ', exonStartA
	#print 'Exon ends: ', exonEndsA
	start = pol2.query(chrom, target_gene.txStart - 30, target_gene.txStart + 300, 1)
	end = pol2.query(chrom, target_gene.txStart + 301, target_gene.txEnd, 1)
	if start and end:
		if start[0]['mean'] > 0 and end[0]['mean'] > 0:
			trScores[target_gene.name] = (start[0]['mean'])/ (end[0]['mean'])
			if trScores[target_gene.name] > maxScore:
				maxScore = trScores[target_gene.name]
	print("Gene: " + target_gene.name + ", pol2: ")
	print(trScores[target_gene.name])

