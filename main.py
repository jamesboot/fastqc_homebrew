# Script for testing "homebrew" fastqc functions

# Import modules
import functions.ReadQScores as rqs
import matplotlib.pyplot as plt

# Specify test file dir
test1 = "/Users/jamesboot/Documents/9.Genome Centre Files/GC-UP-10453/Paired-end-sequencing-trial/bcl2fastq/GC-UP-10543-T1837-700kReadsDiscarded_S1_L001_R1_001.fastq"
print('File is: ', test1)

# Run read q scores function
print('Reading Q Scores from file...')
result1 = rqs.readQscores(test1)

# Plot result
plt.hist(result1)
