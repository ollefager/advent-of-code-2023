import re

def main():
    with open('input.txt', 'r') as file:
        sumOfShortestDistancesBetweenEveryPair = 0
        universeMap = [line.replace('\n', '') for line in file]
        galaxyExpansions = 1000000

        rowExpandedMap    = []
        columnExpandedMap = []

        for index, line in enumerate(universeMap):
            if not re.findall('#', line):
                print(index)
                rowExpandedMap.append(index)

        numberOfColumns = len(universeMap[0])

        print("")

        for i in range(numberOfColumns):
            column = [line[i] for line in universeMap]
            if '#' not in column:
                columnExpandedMap.append(i)
                print(i)
                

        galaxyCoordinatesList = []

        for index, line in enumerate(universeMap):
            galaxyCoordinatesList.extend([[(index, m.start(0))] for m in re.finditer('#', line)])
            print(line)

        for i in range(len(galaxyCoordinatesList) - 1):
            for j in range(i + 1, len(galaxyCoordinatesList)):

                x = galaxyCoordinatesList[i][0][0]
                y = galaxyCoordinatesList[i][0][1]

                x2 = galaxyCoordinatesList[j][0][0]
                y2 = galaxyCoordinatesList[j][0][1]

                numberOfRowExpansions    = 0
                numberOfColumnExpansions = 0

                if x < x2:
                    for rowExpansion in rowExpandedMap:
                        if x < rowExpansion < x2:
                            numberOfRowExpansions += 1
                    xdist = x2 - x + numberOfRowExpansions * (galaxyExpansions - 1)
                elif x > x2:
                    for rowExpansion in rowExpandedMap:
                        if x2 < rowExpansion < x:
                            numberOfRowExpansions += 1
                    xdist = x - x2 + numberOfRowExpansions * (galaxyExpansions - 1)
                else: # same coordinate
                    xdist = 0

                if y < y2:
                    for columnExpansion in columnExpandedMap:
                        if y < columnExpansion < y2:
                            numberOfColumnExpansions += 1
                    ydist = y2 - y + numberOfColumnExpansions * (galaxyExpansions - 1)
                elif y > y2:
                    for columnExpansion in columnExpandedMap:
                        if y2 < columnExpansion < y:
                            numberOfColumnExpansions += 1
                    ydist = y - y2 + numberOfColumnExpansions * (galaxyExpansions - 1)
                else: # same coordinate
                    ydist = 0

                distance = xdist + ydist
                sumOfShortestDistancesBetweenEveryPair += distance
                
        print(sumOfShortestDistancesBetweenEveryPair)

if __name__ == '__main__':
    main() 