import math
import random
import sys
import string

def loadSeq(fileName):
    dnaFile = open(fileName,'r')
    seqList = []
    dna = ""
    for line in dnaFile:
        if line[0] == ">":
            seqList.append(line[1:-1])
        if line[0] != ">":
            dna += line.replace("\n","")
    seqList.append(dna)
    dnaFile.close()
    return seqList


def readCommand(command):
    #Check flags
    if "-i" not in command:
        print("Missing -i arguement")
        sys.exit()
    if "-j" not in command:
        print("Missing -j arguement")
        sys.exit()
    if "-p" not in command:
        print("Missing -p arguement")
        sys.exit()
    if "-atype" not in command:
        print("Missing -atype arguement")
        sys.exit()
    if "-o" not in command:
        print("Missing -o arguement")
        sys.exit()

    #Check seq1
    if command.index("-i") < len(command)-1:
        seq1Name = command[command.index("-i")+1]
        if seq1Name[0] == "-":
            print("Missing sequence file name after -i")
            sys.exit()
    else:
        print("Missing sequence file name after -i")
        sys.exit()

    #Check seq2
    if command.index("-j") < len(command)-1:
        seq2Name = command[command.index("-j")+1]
        if seq2Name[0] == "-":
            print("Missing sequence file name after -j")
            sys.exit()
    else:
        print("Missing sequence file name after -j")
        sys.exit()
    
    #Check sequence type
    if command.index("-p") < len(command)-1:
        seqType = command[command.index("-p")+1]
        if seqType[0] == "-":
            print("Missing sequence type after -p")
            sys.exit()
        elif seqType != "T" and seqType != "F":
            print("Invalid value for sequence type")
            sys.exit()
    else:
        print("Missing sequence type after -p")
        sys.exit()

    #Check alignment type
    if command.index("-atype") < len(command)-1:
        alignType = command[command.index("-atype")+1]
        if alignType[0] == "-":
            print("Missing alignment type after -atype")
            sys.exit()
        elif alignType != "G" and alignType != "S" and alignType != "L":
            print("Invalid value for alignment type")
            sys.exit()
    else:
        print("Missing alignment type after -atype")
        sys.exit()
    
    #Check outfile
    if command.index("-o") < len(command)-1:
        outFile= command[command.index("-o")+1]
        if outFile[0] == "-":
            print("Missing output file name after -o")
            sys.exit()
    else:
        print("Missing output file name after -o")
        sys.exit()
    
    return [seq1Name,seq2Name,seqType,alignType,outFile]
