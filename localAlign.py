import sys
from score import*

def initMatrix(row,col):
    #create grid with (0,0,0)
    matrix = [[(0,0,0) for j in range(col)] for i in range(row)]
    return matrix

def initLocalMatrix(row,col):
    matrix = initMatrix(row,col)
    #init first row
    i = 1
    j = 0
    while i>j and i<row:
        matrix[i][j] = (0,i-1,j)
        i+=1
    #init first col
    i = 0
    j = 1
    while j>i and j<col:
        matrix[i][j] = (0,i,j-1)
        j+=1
    return matrix

def fillLocalMatrix(seq1,seq2,matrix,seqType):
    #fill from up to bottom, left to right
    i = 1
    while i<= len(seq1):
        j = 1
        while j<= len(seq2):
            upGrid = (matrix[i][j-1][0]+gapScore(seqType),i,j-1)
            leftGrid = (matrix[i-1][j][0]+gapScore(seqType),i-1,j)
            diagonalGrid = (matrix[i-1][j-1][0]+score(seq1[i-1],seq2[j-1],seqType),i-1,j-1)
            
            matrix[i][j] = upGrid
            
            if  leftGrid[0]>matrix[i][j][0]:
                matrix[i][j] = leftGrid
            if diagonalGrid[0]>matrix[i][j][0]:
                matrix[i][j] = diagonalGrid
            if matrix[i][j][0] < 0:
                matrix[i][j] = (0,matrix[i][j][1],matrix[i][j][2])
            j+=1
        i+=1
    return matrix

def traceBackScore(seq1,seq2,matrix):
    maxScore = (0,0,0)
    maxScoreList = []
    i = 0
    #find the max score list
    while i<= len(seq1) :
        j = 1
        while j<= len(seq2):
            if matrix[i][j][0] > maxScore[0]:
                maxScore = (matrix[i][j][0],i,j)
                maxScoreList = [maxScore]
            elif matrix[i][j][0] == maxScore[0]:
                maxScoreList.append((matrix[i][j][0],i,j))
            j+=1
        i+=1

    finalList = []
    #trace back with each score
    for item in maxScoreList:
        i = item[1]
        j = item[2]
        grid = matrix[i][j]
        newSeq1 = ""
        newSeq2 = ""
        match = 0
        while grid[0] != 0:
            if matrix[i][j][1] == i:
                newSeq1 = "_"+newSeq1
                newSeq2 = seq2[j-1]+newSeq2
                grid = matrix[grid[1]][grid[2]]
                j-=1
            elif matrix[i][j][2] == j:
                newSeq1 = seq1[i-1]+newSeq1
                newSeq2 = "_"+newSeq2
                grid = matrix[grid[1]][grid[2]]
                i-=1
            else:
                newSeq1 = seq1[i-1]+newSeq1
                newSeq2 = seq2[j-1]+newSeq2
                if seq1[i-1] == seq2[j-1]:
                    match+=1
                grid = matrix[grid[1]][grid[2]]
                i-=1
                j-=1
        finalList.append((newSeq1,newSeq2,maxScore[0],match,i,j))
    return finalList


def localAlign(seq1,seq2,seqType):
    matrix = fillLocalMatrix(seq1,seq2,initLocalMatrix(len(seq1)+1,len(seq2)+1),seqType)
    return traceBackScore(seq1,seq2,matrix)
