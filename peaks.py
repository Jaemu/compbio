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
peaks = pickle.load(open('/Users/JME/Documents/CSE549/peak_data.p', 'rb'))

for i in peaks.keys():
	for j in peaks[i].keys():
		if len(peaks[i][j].keys()) > 1:
			print(str(i) + ": " + "gene: " + str(j) + ", number of peaks: " + str(len(peaks[i][j].keys())))

