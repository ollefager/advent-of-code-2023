import regex as re
import itertools

def main():

    lowestLocation = None

    with open('input.txt', 'r') as file:
        fileContents  = file.read()
        seedString    = fileContents.split(":")[1]
        mapString     = fileContents.split(":")[2:]

        seedsList     = re.findall('[0-9]+', seedString)
        seedStartList = list(map(int, seedsList[::2]))
        seedRangeList = list(map(int, seedsList[1::2]))

        seedTupleList = sorted(zip(seedStartList, seedRangeList), key=lambda x: x[0])
        seedStartList, seedRangeList = zip(*seedTupleList)

        seedLowest  = min(seedStartList)
        seedHighest = max(seedStartList) + max(seedRangeList)
        
        location = 0
        lowestLocation = None

        refactoredMap = structureMap(mapString)

        while lowestLocation is None:
            
            seedNumber = mapToSeed(location, refactoredMap)

            if seedNumber < seedLowest or seedNumber > seedHighest:
                location += 1
                continue

            left = 0
            right = len(seedStartList) - 1

            while left <= right:
                mid = (left + right) // 2
                seedStart = seedStartList[mid]
                seedRange = seedRangeList[mid]
                seedEnd = (seedStart + seedRange)

                if seedStart <= seedNumber < seedEnd:
                    lowestLocation = location
                    break
                elif seedNumber < seedStart:
                    right = mid - 1
                else:
                    left = mid + 1

            location += 1
        
        print(lowestLocation)


def mapToSeed(location, refactoredMap):
    currentMapValue = location

    for mapSegment in refactoredMap:
        left = 0
        right = len(mapSegment) - 1

        while left <= right:
            mid = (left + right) // 2
            mapTruple = mapSegment[mid]
            source, destination, rangeJump = map(int, mapTruple)

            if source <= currentMapValue < (source + rangeJump):
                destinationRange = currentMapValue - source
                currentMapValue = destination + destinationRange
                break
            elif currentMapValue < source:
                right = mid - 1
            else:
                left = mid + 1

    return currentMapValue

def structureMap(mapString):
    refactoredMap   = []
    pattern         = re.compile('[0-9]+')

    for mapSegment in reversed(mapString):
        segmentMap = []  # Add an empty list for each mapSegment

        lines    = mapSegment.split("\n")

        for line in lines:
            mapTruple = pattern.findall(line) if pattern.findall(line) else None
            
            if mapTruple == None:
                continue
            else:
                segmentMap.append(mapTruple)

        segmentMap.sort(key=lambda x: int(x[0]))
        refactoredMap.append(segmentMap)

    return refactoredMap

if __name__ == '__main__':
    main()
