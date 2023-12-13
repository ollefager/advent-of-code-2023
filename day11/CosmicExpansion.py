import re

def main():
    with open('input.txt', 'r') as file:
        sumOfShortestDistancesBetweenEveryPair = 0
        universeMap = [line.replace('\n', '') for line in file]
        expandedMap = []

        for index, line in enumerate(universeMap):
            if re.findall('#', line):
                expandedMap.append(line)
            else:
                print(index)
                expandedMap.extend([line, line])

        print("")

        k = 0
        numberOfColumns = len(expandedMap[0])

        for i in range(numberOfColumns):
            column = [line[k] for line in expandedMap]
            if '#' not in column:
                for j in range(len(expandedMap)):
                    line = expandedMap[j]
                    expandedMap[j] = line[:k+1] + '.' + line[k+1:]
                print(k)
                k += 1
            k += 1

        galaxyCoordinatesList = []

        for index, line in enumerate(expandedMap):
            galaxyCoordinatesList.extend([[(index, m.start(0))] for m in re.finditer('#', line)])
            print(line)

        for i in range(len(galaxyCoordinatesList) - 1):
            for j in range(i + 1, len(galaxyCoordinatesList)):
                x = galaxyCoordinatesList[i][0][0]
                y = galaxyCoordinatesList[i][0][1]

                x2 = galaxyCoordinatesList[j][0][0]
                y2 = galaxyCoordinatesList[j][0][1]

                distance = abs(y2 - y) + abs(x2 - x)

                sumOfShortestDistancesBetweenEveryPair += distance
                
        print(sumOfShortestDistancesBetweenEveryPair)

if __name__ == '__main__':
    main() 