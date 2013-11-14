compbio
=======

Programming challenges from CSE549: Computational Biology


About:
- General repository for both homework problems and final project for CSE 549 (http://www.cs.stonybrook.edu/~skiena/549/)

=======

Semester Project:
- Background:
The goal of our research, in collaboration with Pf. MacCarthy, is to provide independent support for recent findings that PolII transcription factor AID is responsible for off-target somatic mutations in genes during production of antibodies as well as identify genes where these mutations are likely to occur.  This data has already been independently produced in mice by breeding mice with no other mutation mechanism besides AID (eg. proteins involved in DNA repair) and identifying genes which produced AID signature mutations.  

Important Data Files:
- hg19.txt: Contains gene data including start position, stop position, chromosome, and strand (from UCSC genome browser project).
- hg19.bigWig: Contains data from chip-seq experiment for PolII pausing events.  The data is stored as key=position, value=number of PolII observed on position.

Important Scripts:
- hgdata.py: Produces pickle files that contain the above data formatted for fast access and manipulation.
- trscores.py: Produces histograms of TR score frequency for each chromosome.

=======

Homework problems:

- hw2.py: A heuristic for reproducing superstring from unique samples of uniform length to simulate the problem of reconstructing the genome from DNA sampling.
- strcomp.py: Recursive edit distance.  This is bad.
- strincomp.py: Dynamic programming edit distance.  This is less bad.
- rk.py: Implementation of Rabin-Karp string matching algorithm.  This is effective but is not linear.
