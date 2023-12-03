def main():
    REDCUBES   = 12 
    GREENCUBES = 13
    BLUECUBES  = 14

    cubeLimits = {"red" : REDCUBES, "green" : GREENCUBES, "blue" : BLUECUBES}

    file_path = "input.txt"
    sum       = 0
    powerSum  = 0

    with open(file_path, "r") as file:
        for index, line in enumerate(file, start=1):

            gameData = obtainGameData(line)

            minimumSet   = obtainMinumumSet(gameData)
            partPowerSum = 0

            for color, minimumSetValue in minimumSet.items():
                if partPowerSum == 0:
                    partPowerSum = minimumSetValue
                else:
                    partPowerSum *= minimumSetValue

            powerSum += partPowerSum 
            
            if isSanityCheckPassed(gameData, cubeLimits):
                sum += index

    print(sum)
    print(powerSum)

def obtainGameData(string):
    string = string.strip()

    # Extract content after ":"
    content = string.split(":")[1]

    # Split content into sections
    sections = content.split(";")

    game = []

    for section in sections:
        sets = section.split(",")
        element = {}
        
        for set in sets:
            number, color = set[1:].split(" ")
            element[color] = int(number)

        game.append(element)

    return game

def isSanityCheckPassed(dataSet, cubeLimits):
    for data in dataSet:
        for color, dataValue in data.items():
            if cubeLimits[color] < dataValue:
                return False
    
    return True

def obtainMinumumSet(dataSet):
    minimumSet = {}
    for data in dataSet:
        for color, dataValue in data.items():
            if color in minimumSet:
                if dataValue > minimumSet[color]:
                    minimumSet[color] = dataValue
            else:
                minimumSet[color] = dataValue
           
    return minimumSet

if __name__ == "__main__":
    main()
