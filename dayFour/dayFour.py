import numpy as np

def createMatrix(fileName):
    with open(fileName, 'r') as f:
        return [list(map(str, list(points))) for points in f.read().split('\n') ]

def removeRolls(matrix):
    totalRemoved = 0    
    while True:
        numRolls, rollPoints = findRolls(matrix)
        if numRolls == 0:
            return totalRemoved
        else:
            for x,y in rollPoints: 
                matrix[x,y] = '.'
            totalRemoved += numRolls

def findRolls(matrix):
    rows, cols = matrix.shape
    matchCase = 0
    matchRolls = []
    for row in range(rows):
        for col in range(cols):
            if matrix[row, col] == '@':
                neighbors = []
                for dr in range(-1,2):
                    for dc in range(-1,2):
                        if dr == 0 and dc == 0:
                            continue
                        nRow, nCol = row + dr, col + dc

                        if 0 <= nRow < rows and 0 <= nCol < cols:
                            if matrix[nRow, nCol] == '@':
                                neighbors.append(matrix[nRow, nCol])
                if len(neighbors) < 4:
                    matchRolls.append((row, col))
                    matchCase +=1
    return matchCase, matchRolls                   


def testCase():
    passes = True
    matrix = np.array(createMatrix('testIngest.txt'))
    actualOutputOne,_  = findRolls(matrix)
    print(f"\nExpected Output: 13\n\nActual Output:{actualOutputOne}\n")
    if actualOutputOne != 13:
        passes =  False
    totalRemoved = removeRolls(matrix)
    if totalRemoved != 43:
        passes = False
    if passes:
        return True
    else:
        print("Test Case failed:")
        print("Scenario 1:\nExpected Output 13\n")
        print(f"Actual Output: {actualOutputOne}\n\n")
        print("Scenario 2:\nExpected Output 43\n")
        print(f"Actual Output: {totalRemoved}")



def prodRun():
    matrix = np.array(createMatrix('ingest.txt'))
    actualOutput,_ = findRolls(matrix)
    print(f"Output of part 1 is {actualOutput}")
    print(removeRolls(matrix))

if testCase():
    prodRun()