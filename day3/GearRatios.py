def main():
    sumPartNumbers               = 0
    sumGearRatio                 = 0
    currentPartNumber            = ''
    isPartNumberAdjacentToSymbol = False
    symbolString                 = '*@-+#%=/$&'

    with open('input.txt', 'r') as file:

        # Convert data to a 2d array
        dataInput    = [list(line.rstrip('\n')) for line in file]

        # Main struct to store all information
        mapInfo      = {"dataInput"    : dataInput,
                        "symbolString" : symbolString,
                        "temporaryStar": [],
                        "permanentStar": [],
                        "maxRow"       : len(dataInput), 
                        "maxColumn"    : len(dataInput[0])} # I already know the input is a square matrix
        
        # Iterate through each element in the 2d array
        for row in range(mapInfo["maxRow"]):
            for column in range(mapInfo["maxColumn"]):

                # Update mapInfo for new element
                mapInfo["currentRow"]     = row
                mapInfo["currentColumn"]  = column
                currentElement            = mapInfo["dataInput"][row][column]

                if (currentElement.isdigit()):
                    currentPartNumber += currentElement # StringParse the partNumber

                    # Check if element is adjacent to a symbol
                    if symbolIsAdjacent(mapInfo):
                        isPartNumberAdjacentToSymbol = True

                    # Check if currentPart number is complete
                    if isPartNumberComplete(mapInfo):
                        if isPartNumberAdjacentToSymbol:
                            sumPartNumbers += int(currentPartNumber)

                            # Move temporary stars to permanent stars. Map partNumber to permanent stars 
                            appendTemporaryStarToPermanentStar(mapInfo, currentPartNumber)

                        # Reset variables for next partNumber
                        mapInfo["temporaryStar"] = []
                        currentPartNumber = ''
                        isPartNumberAdjacentToSymbol = False

    print(sumPartNumbers)
    
    for starInfo in mapInfo["permanentStar"]:
        # Determines if star is a gear
        if len(starInfo["partNumberList"]) == 2:
            sumGearRatio += int(starInfo["partNumberList"][0]) * int(starInfo["partNumberList"][1])
    print(sumGearRatio)

def symbolIsAdjacent(mapInfo):
    currentRow       = mapInfo["currentRow"]
    currentColumn    = mapInfo["currentColumn"]
    symbolString     = mapInfo["symbolString"]
    isSymbolAdjacent = False

    adjacentPositions = [(currentRow - 1, currentColumn - 1), (currentRow - 1, currentColumn),
                         (currentRow - 1, currentColumn + 1), (currentRow, currentColumn - 1),
                         (currentRow, currentColumn + 1),     (currentRow + 1, currentColumn - 1),
                         (currentRow + 1, currentColumn),     (currentRow + 1, currentColumn + 1)]
    
    # Messy multi purpose segment but solves for both Part 1 and Part 2
    for row, column in adjacentPositions:
        if 0 <= row < mapInfo["maxRow"] and 0 <= column < mapInfo["maxColumn"]:
            if mapInfo["dataInput"][row][column] in symbolString:
                if mapInfo["dataInput"][row][column] == "*":
                    mapInfo["temporaryStar"].append((row, column))
                isSymbolAdjacent = True

    return isSymbolAdjacent

def isPartNumberComplete(mapInfo):
    currentColumn = mapInfo["currentColumn"]
    currentRow    = mapInfo["currentRow"]

    # We assume that partNumbers can't continue to the next row
    if (currentColumn + 1) == mapInfo["maxColumn"]:
        return True
    # Check if next column is not a digit
    elif not (mapInfo["dataInput"][currentRow][currentColumn + 1].isdigit()):
        return True
    else: 
        return False
    
def appendTemporaryStarToPermanentStar(mapInfo, currentPartNumber):
    # Remove duplicate tuples
    mapInfo["temporaryStar"] = list(set(mapInfo["temporaryStar"]))

    for tuple in mapInfo["temporaryStar"]:
        # Check if the coordinates can be found
        coordinatesFound = False

        # Add partNumber to existing star
        for starInfo in mapInfo["permanentStar"]:
            if tuple == starInfo["coordinates"]:
                starInfo["partNumberList"].append(currentPartNumber)
                coordinatesFound = True
                break
        
        # Create a new star with a mapped partNumber
        if not coordinatesFound:
            starInfo = {"coordinates" : tuple,
                        "partNumberList" : [currentPartNumber]} 
            mapInfo["permanentStar"].append(starInfo)

if __name__ == '__main__':
    main()