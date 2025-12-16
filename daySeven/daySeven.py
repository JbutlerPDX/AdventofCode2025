
def loadContent(fileName):
    with open(fileName, 'r') as f:
        return f.read().splitlines()
    
def createMatrix(content):
    matrix = []
    for line in content:
        matrix.append([point for point in line])
    return matrix

def tachyonTrace(content):
    tachyonArray = []
    totalSplits = 0
    tachyonArray = createMatrix(content)
    for i in range(len(tachyonArray)):
        if i == 0:
            tachyonArray[1][tachyonArray[i].index('S')] = '|'
        elif i > 1:
            beamInds = [i for i, state in enumerate(tachyonArray[i-1]) if state == '|']
            splitInds = [i for i, letter in enumerate(tachyonArray[i]) if letter == '^']
            splitStates = list(set(beamInds) & set(splitInds))
            for point in beamInds:
                if point not in splitStates:
                    tachyonArray[i][point] = '|'
            if splitStates:
                for split in splitStates:
                    tachyonArray[i][split - 1] = tachyonArray[i][split + 1] = '|'
                    totalSplits += 1

    return totalSplits

def getTimelines(content):
    totalTimelines = [0] * len(content[0])
    tachyonArray = createMatrix(content)
    pointer = tachyonArray[0].index('S')
    totalTimelines[pointer] = 1
    for i in range(1,len(tachyonArray)):
        splitInds = [i for i, letter in enumerate(tachyonArray[i]) if letter == '^']
        if not splitInds:
            continue
        else:
            for ind in splitInds:
                totalTimelines[ind-1] += totalTimelines[ind]
                totalTimelines[ind+1] += totalTimelines[ind]
                totalTimelines[ind] = 0
    return sum(totalTimelines)


def unitTest(method,ingest, expected):
    output = method(ingest)
    return output, output == expected

if __name__ == "__main__":
    passes = True
    testContent = loadContent('testIngest.txt')
    print("Running test run\n===\n")
    actualOutputOne, passes = unitTest(tachyonTrace,testContent, 21)
    actualOutputTwo, passes = unitTest(getTimelines,testContent, 40)
    print("Expected Output for test one: 21\n")
    print(f"Actual Output: {actualOutputOne}\n===\n")
    print("Expected Output for test two: 40\n")
    print(f"Actual Output: {actualOutputTwo}\n===\n")
    if not passes:
        print("Test runs fails")
        exit()
    else:
        prodContent = loadContent('ingest.txt')
        print("Test runs succeed. Running prod run")
        print(f"Results from first run: {tachyonTrace(prodContent)}")
        print(f"Results from second run: {getTimelines(prodContent)}")