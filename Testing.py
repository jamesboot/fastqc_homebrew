# Script for testing "homebrew" fastqc functions

from .ReadQScores import *

test1 = "/Users/jamesboot/Documents/9.Genome Centre Files/1M-GC-CF-9830-11TMGA-T_S20_L001_R1_001.fastq"
test2 = "/Users/jamesboot/Documents/9.Genome Centre Files/GC-SST-10001-C2-w3-1-7-22_S23_L001_R1_001.fastq"

result1 = readQscores(test1)
result2 = readQscores(test2)

import matplotlib.pyplot as plt

plt.hist(result1)
plt.hist(result2)