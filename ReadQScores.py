# Function for:
# 1.Reading a fastq file
# 2.Extract the Q scores 
# 3.Calculate average Q score of each read

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