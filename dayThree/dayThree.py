def solve(battery, maxLen):
    
    total = 0 
    for batt in battery:
        battLen = len(batt)
        joltStack = [[0 for j in range(maxLen + 1)] for i in range(battLen + 1)]
        for i in range(battLen):
            for j in range(maxLen + 1):
                joltStack[i + 1][j] = max(joltStack[i + 1][j], joltStack[i][j])
                if j < maxLen:
                    joltStack[i + 1][j + 1] = max(joltStack[i + 1][j + 1], 10 * joltStack[i][j] + batt[i])        
        total += joltStack[battLen][maxLen]
    
    return total



def createMatrix(fileName):
    with open(fileName, 'r') as f:
        return [list(map(int, list(rng))) for rng in f.read().split('\n')]


def testCase():
    testMatrix = createMatrix('testIngest.txt')
    expectedOutput1, expectedOutput2 =357, 3121910778619
    actualOutput1 = solve(testMatrix, 2)
    actualOutput2 = solve(testMatrix, 12)    
    if expectedOutput1 == actualOutput1 and expectedOutput2 == actualOutput2:
        print("Test case successful")
    else:
        print(f"Error in code: \n===\nExpected Output Case 1: {expectedOutput1}\nActual Output: {actualOutput1}\n\n===\nExpected Output Case 2: {expectedOutput2}\nActual Output: {actualOutput2}")   
            

def ProdRun():
    matrix = createMatrix('ingest.txt')
    expectedOutput = 17244
    actualOutput = solve(matrix, 2)
    if expectedOutput == actualOutput:
        print("Case 1 passes")
    print(solve(matrix, 12))


testCase()
ProdRun()