#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 14:00:23 2023

@author: jamesboot
"""

# Here I write my own function for reading a fastq file and extracting the Q scores from it

def fastQC(infile):

    sequences = []
    qualities = []
    
    with open(infile) as file:
        while True:
            # Skip the first line (read name)
            file.readline()
            # Read the sequence on the next line
            seq = file.readline().rstrip()
            # Skip the placeholder line
            file.readline()
            # Read the base quality line
            qual = file.readline().rstrip()
            # Break the loop if line is 0
            if len(seq) == 0:
                break
            sequences.append(seq)
            qualities.append(qual)
    
    readQvals = []
    
    # Loop through all read qualities and determine average read score of every read
    for i in range(len(qualities)):
        Qvals = []
        
        # Loop through the quality ASCII codings to extract score
        for x in range(len(list(qualities[i]))):
            Qvals.append(ord(list(qualities[i])[x])-33)
            
        readQvals.append(sum(Qvals)/len(Qvals))
    
    # Return vector of Q scores for every read
    return readQvals


test1 = "/Users/jamesboot/Documents/9.Genome Centre Files/1M-GC-CF-9830-11TMGA-T_S20_L001_R1_001.fastq"
test2 = "/Users/jamesboot/Documents/9.Genome Centre Files/GC-SST-10001-C2-w3-1-7-22_S23_L001_R1_001.fastq"

result1 = fastQC(test1)
result2 = fastQC(test2)

import matplotlib.pyplot as plt

plt.hist(result1)
plt.hist(result2)
