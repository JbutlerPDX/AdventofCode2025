import re
import bisect

def getRanges(fileContent):
    return list(re.findall(r"(\d+)-(\d+)", fileContent))

def loadContent(fileName):
    with open(fileName, 'r') as f:
        return f.read() 

def findSpoiled(fileContent):

    unspoiledFood = []
    idRanges = getRanges(fileContent)
    foodId = list(re.findall(r"^(\d+)$", fileContent, re.MULTILINE))

    for food in foodId:
        spoiled = True
        for idRange in idRanges:
            if int(idRange[0]) <= int(food) <= int(idRange[1]):
                spoiled = False
        if not spoiled:
            unspoiledFood.append(food)
    
    return len(unspoiledFood)

def getAllUnspoiled(fileContent):
    foodRanges = []
    total = 0
    idRanges = getRanges(fileContent)
    intervals = sorted((int(start), int(end)) for start,end in idRanges)

    idStart,idEnd = intervals[0]

    for rStart, rEnd in intervals[1:]:
        if rStart <= idEnd + 1:
            idEnd = max(idEnd, rEnd)
        else:
            foodRanges.append((idStart, idEnd))
            idStart,idEnd = rStart,rEnd
    foodRanges.append((idStart,idEnd))
    for idStart, idEnd in foodRanges:
        total += (idEnd - idStart + 1)
    return total        
    
        

    

def unitTest(method,ingest, expected):
    output = method(ingest)
    return output, output == expected

if __name__ == "__main__":
    passes = True
    testContent = loadContent('testIngest.txt')
    print("Running test run\n===\n")
    actualOutputOne, passes = unitTest(findSpoiled,testContent, 3)
    actualOutputTwo, passes = unitTest(getAllUnspoiled,testContent, 14)
    print("Expected Output for test one: 3\n")
    print(f"Actual Output: {actualOutputOne}\n===\n")
    print("Expected Output for test two: 14\n")
    print(f"Actual Output: {actualOutputTwo}\n===\n")
    if not passes:
        print("Test runs fails:\n===\n")
        exit()
    else:
        prodContent = loadContent('ingest.txt')
        print("Test runs succeed. Running prod run")
        print(f"Results from first run: {findSpoiled(prodContent)}")
        print(f"Results from second run: {getAllUnspoiled(prodContent)}")


