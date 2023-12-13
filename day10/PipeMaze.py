import re

def main():
    with open("input.txt", 'r') as file:
        pipelineMap   = [list(line.strip()) for line in file]

        startPositionI, startPositionJ = next((i, j) for i, line in enumerate(pipelineMap) for j, char in enumerate(line) if char == 'S')

        distance = calculateDistanceFurthestTile(pipelineMap, startPositionI, startPositionJ)

        print(distance)

def calculateDistanceFurthestTile(pipelineMap, startPositionI, startPositionJ):
        
    previousI         = startPositionI
    previousJ         = startPositionJ
    i                 = startPositionI
    j                 = startPositionJ

    totalDistance     = 0

    while True:

        if pipelineMap[i][j] == 'S':
            currentChar = determineStartCharacter(pipelineMap, startPositionI, startPositionJ)
        else: 
            currentChar = pipelineMap[i][j]

        if currentChar == '|':
            if (i + 1, j) == (previousI, previousJ):
                print("Up")
                previousI, previousJ = i, j
                i = i - 1
            else:
                print("Down")
                previousI, previousJ = i, j
                i = i + 1
        elif currentChar == '-':
            if (i, j + 1) == (previousI, previousJ):
                print("Left")
                previousI, previousJ = i, j
                j = j - 1
            else:
                print("Right")
                previousI, previousJ = i, j
                j = j + 1
        elif currentChar == 'L':
            if (i, j + 1) == (previousI, previousJ):
                print("Up")
                previousI, previousJ = i, j
                i = i - 1
            else:
                print("Right")
                previousI, previousJ = i, j
                j = j + 1
        elif currentChar == 'J':
            if (i, j - 1) == (previousI, previousJ):
                print("Up")
                previousI, previousJ = i, j
                i = i - 1
            else:
                print("Left")
                previousI, previousJ = i, j
                j = j - 1
        elif currentChar == 'F':
            if (i, j + 1) == (previousI, previousJ):
                print("Down")
                previousI, previousJ = i, j
                i = i + 1
            else:
                print("Right")
                previousI, previousJ = i, j
                j = j + 1
        elif currentChar == '7':
            if (i, j - 1) == (previousI, previousJ):
                print("Down")
                previousI, previousJ = i, j
                i = i + 1
            else:
                print("Left")
                previousI, previousJ = i, j
                j = j - 1
        else:
            print("Error: Invalid character")

        totalDistance += 1

        if pipelineMap[i][j] == 'S':
            return totalDistance/2 
            
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