import sys
import random
from load import*
from globalAlign import*
from semiglobalAlign import*
from localAlign import*

def main():
    
    #get command args
    commandArgs = readCommand(sys.argv)

    #load sequence
    seq1 = loadSeq(commandArgs[0])
    seq2 = loadSeq(commandArgs[1])
    
    #seq type
    seqType = commandArgs[2]

    #alignment
    alignType = commandArgs[3]
    result = []
    if alignType == "G":
        result = globalAlign(seq1[1],seq2[1],seqType)
    elif alignType == "S":
        result = semiglobalAlign(seq1[1],seq2[1],seqType)
    else:
        result = localAlign(seq1[1],seq2[1],seqType)

    #output
    output = open(commandArgs[4],'w')
    for item in result:
        tempSeq1 = item[0]
        tempSeq2 = item[1]
        while len(tempSeq1) > 60:
            startSeq1 = item[4]
            endSeq1 = startSeq1+len(item[0][0:60].replace("_",""))
            output.write(seq1[0]+": "+str(startSeq1)+" "+tempSeq1+" "+str(endSeq1)+"\n")
            startSeq1 = endSeq1
            tempSeq1 = tempSeq1[60:]
            startSeq2 = item[5]
            endSeq2 = startSeq2+len(item[0][0:60].replace("_",""))
            output.write(seq1[0]+": "+str(startSeq2)+" "+tempSeq2+" "+str(endSeq2)+"\n")
            startSeq2 = endSeq2
            tempSeq2 = tempSeq2[60:]
        output.write(seq1[0]+": "+str(item[4])+" "+item[0]+" "+str(item[4]+len(item[0][0:60].replace("_","")))+"\n")
        output.write(seq2[0]+": "+str(item[5])+" "+item[1]+" "+str(item[5]+len(item[0][0:60].replace("_","")))+"\n")
        output.write("\n")
        output.write("Score: "+str(item[2])+"\n")
        output.write("Identities: "+str(item[3])+"/"+str(len(item[0]))+" ("+str(item[3]*100//len(item[0]))+"%)")
    output.close()

main()
