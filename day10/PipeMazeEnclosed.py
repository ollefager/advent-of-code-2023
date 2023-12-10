import copy
import sys

def main():
    sys.setrecursionlimit(80000)
    print(sys.getrecursionlimit())
    with open("input.txt", 'r') as file:
        pipelineMap   = [list(line.strip()) for line in file]

        startPositionI, startPositionJ = next((i, j) for i, line in enumerate(pipelineMap) for j, char in enumerate(line) if char == 'S')

        enclosedMap   = obtainEnclosedMap(pipelineMap, startPositionI, startPositionJ)
        enclosedTiles = obtainNumberOfEnclosedTiles(enclosedMap)

        print(enclosedTiles)
        
                
def obtainNumberOfEnclosedTiles(enclosedMap):

    copyEnclosedMap       = copy.deepcopy(enclosedMap)
    progressEnclosedMap   = copy.deepcopy(enclosedMap)
    numberOfEnclosedTiles = 0

    for i, line in enumerate(enclosedMap[::2]):
        for j, tile in enumerate(line[::2]):
            if tile != 1:
                copyEnclosedMap = copy.deepcopy(progressEnclosedMap)
                if isEnclosedTile(i * 2, j * 2, copyEnclosedMap):
                    progressEnclosedMap = copy.deepcopy(copyEnclosedMap)
                    numberOfEnclosedTiles += 1
                    
                
    return numberOfEnclosedTiles

def isEnclosedTile(i, j, enclosedMap):

    isNorthEnclosed = False if i - 1 < 0 else True
    isSouthEnclosed = False if i + 1 >= len(enclosedMap) else True
    isWestEnclosed  = False if j - 1 < 0 else True
    isEasthEnclosed = False if j + 1 >= len(enclosedMap[0]) else True

    enclosed = isNorthEnclosed and isSouthEnclosed and isWestEnclosed and isEasthEnclosed

    enclosedMap[i][j] = 1

    if not enclosed:
        return False
    else:
        if enclosedMap[i - 1][j]:
            isNorthEnclosed = True
        else:
            isNorthEnclosed = isEnclosedTile(i - 1, j, enclosedMap)
        if enclosedMap[i + 1][j]:
            isSouthEnclosed = True
        else:
            isSouthEnclosed = isEnclosedTile(i + 1, j, enclosedMap)
        if enclosedMap[i][j - 1]:
            isWestEnclosed = True
        else:
            isWestEnclosed = isEnclosedTile(i, j - 1, enclosedMap)
        if enclosedMap[i][j + 1]:
            isEasthEnclosed = True
        else:
            isEasthEnclosed = isEnclosedTile(i, j + 1, enclosedMap)

    return isNorthEnclosed and isSouthEnclosed and isWestEnclosed and isEasthEnclosed

def obtainEnclosedMap(pipelineMap, startPositionI, startPositionJ):
        
    previousI         = startPositionI
    previousJ         = startPositionJ
    i                 = startPositionI
    j                 = startPositionJ

    enclosedMap       = [[0] * (2 * len(pipelineMap[0]) - 1) for _ in range((len(pipelineMap) * 2) - 1)]

    while True:

        if pipelineMap[i][j] == 'S':
            currentChar = determineStartCharacter(pipelineMap, startPositionI, startPositionJ)
        else: 
            currentChar = pipelineMap[i][j]

        if currentChar == '|':
            if (i + 1, j) == (previousI, previousJ):
                previousI, previousJ = i, j
                i = i - 1
                enclosedMap[i * 2 + 1][j * 2] = 1
                enclosedMap[i * 2][j * 2] = 1
            else:
                previousI, previousJ = i, j
                i = i + 1
                enclosedMap[i * 2 - 1][j * 2] = 1
                enclosedMap[i * 2][j * 2] = 1
        elif currentChar == '-':
            if (i, j + 1) == (previousI, previousJ):
                previousI, previousJ = i, j
                j = j - 1
                enclosedMap[i * 2][j * 2 + 1] = 1
                enclosedMap[i * 2][j * 2] = 1
            else:
                previousI, previousJ = i, j
                j = j + 1
                enclosedMap[i * 2][j * 2 - 1] = 1
                enclosedMap[i * 2][j * 2] = 1
        elif currentChar == 'L':
            if (i, j + 1) == (previousI, previousJ):
                previousI, previousJ = i, j
                i = i - 1
                enclosedMap[i * 2 + 1][j * 2] = 1
                enclosedMap[i * 2][j * 2] = 1
            else:
                previousI, previousJ = i, j
                j = j + 1
                enclosedMap[i * 2][j * 2 - 1] = 1
                enclosedMap[i * 2][j * 2] = 1
        elif currentChar == 'J':
            if (i, j - 1) == (previousI, previousJ):
                previousI, previousJ = i, j
                i = i - 1
                enclosedMap[i * 2 + 1][j * 2] = 1
                enclosedMap[i * 2][j * 2] = 1
            else:
                previousI, previousJ = i, j
                j = j - 1
                enclosedMap[i * 2][j * 2] = 1
                enclosedMap[i * 2][j * 2 + 1] = 1
        elif currentChar == 'F':
            if (i, j + 1) == (previousI, previousJ):
                previousI, previousJ = i, j
                i = i + 1
                enclosedMap[i * 2 - 1][j * 2] = 1
                enclosedMap[i * 2][j * 2] = 1
            else:
                previousI, previousJ = i, j
                j = j + 1
                enclosedMap[i * 2][j * 2 - 1] = 1
                enclosedMap[i * 2][j * 2] = 1
        elif currentChar == '7':
            if (i, j - 1) == (previousI, previousJ):
                previousI, previousJ = i, j
                i = i + 1
                enclosedMap[i * 2 - 1][j * 2] = 1
                enclosedMap[i * 2][j * 2] = 1
            else:
                previousI, previousJ = i, j
                j = j - 1
                enclosedMap[i * 2][j * 2] = 1
                enclosedMap[i * 2][j * 2 + 1] = 1
        else:
            print("Error: Invalid character")

        if pipelineMap[i][j] == 'S':
            return enclosedMap
            
def determineStartCharacter(pipelineMap, startPositionI, startPositionJ):

    pipeCharacter = None

    if pipelineMap[startPositionI - 1][startPositionJ] in ('|', 'F', '7') and pipelineMap[startPositionI + 1][startPositionJ] in ('|', 'L', 'J'):
        pipeCharacter = '|' 
    elif pipelineMap[startPositionI][startPositionJ - 1] in ('-', 'F', 'L') and pipelineMap[startPositionI][startPositionJ + 1] in ('-', 'J', '7'):
        pipeCharacter = '-'
    elif pipelineMap[startPositionI - 1][startPositionJ] in ('|', 'F', '7') and pipelineMap[startPositionI][startPositionJ + 1] in ('-', '7', 'J') :
        pipeCharacter = 'L'
    elif pipelineMap[startPositionI - 1][startPositionJ] in ('|', 'F', '7') and pipelineMap[startPositionI][startPositionJ - 1] in ('-', 'L', 'F'):
        pipeCharacter = 'J'
    elif pipelineMap[startPositionI + 1][startPositionJ] in ('|', 'L', 'J') and pipelineMap[startPositionI][startPositionJ - 1] in ('-', 'F', 'L'):
        pipeCharacter = '7'
    elif pipelineMap[startPositionI + 1][startPositionJ] in ('|', 'L', 'J') and pipelineMap[startPositionI][startPositionJ + 1] in ('-', 'J', '7'):
        pipeCharacter = 'F'
    else:
        print("Error: Invalid start character")

    return pipeCharacter

if __name__ == "__main__":
    main()