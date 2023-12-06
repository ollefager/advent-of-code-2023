import regex as re

def main():

    lowestLocation = None

    with open('input.txt', 'r') as file:
        fileContents  = file.read()
        seedString    = fileContents.split(":")[1]
        mapString     = fileContents.split(":")[2:]

        seedsList      = re.findall('[0-9]+', seedString)
        
        for seedNumber in seedsList:
            location = mapToLocation(seedNumber, mapString)
            if lowestLocation == None or location < lowestLocation:
                lowestLocation = location

    print(lowestLocation)


def mapToLocation(seedNumber, mapString):

    currentMapValue = int(seedNumber)

    for mapSegment in mapString:

        lines    = mapSegment.split("\n")

        for line in lines:
            mapTruple = re.findall('[0-9]+', line) if re.findall('[0-9]+', line) else None
            
            if mapTruple == None:
                continue
            else:
                destination, source, rangeJump = map(int, mapTruple)
                
                if source <= currentMapValue < (source + rangeJump):
                    destinationRange = currentMapValue - source
                    currentMapValue  = destination + destinationRange
                    break

    return currentMapValue
                    


if __name__ == '__main__':
    main()
