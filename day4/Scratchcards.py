import regex as re

def main():

    totalPoints = 0

    with open('input.txt', 'r') as file:
        maximumNumberOfRows         = len(file.readlines())
        numberOfScratchCardsList    = [1] * maximumNumberOfRows  # Create a list with maximumNumberOfRows elements
        file.seek(0)
        
        for scratchCardIndex, line in enumerate(file):
            winningString, scratchString = line.split(":")[-1].split("|")

            winningNumbers = [m[0] for m in re.finditer('[0-9]+', winningString)]
            scratchNumbers = [m[0] for m in re.finditer('[0-9]+', scratchString)]

            commonNumbers         = list(set(winningNumbers).intersection(scratchNumbers))
            numberOfCommonNumbers = len(commonNumbers)

            if numberOfCommonNumbers != 0:
                totalPoints += 2 ** (numberOfCommonNumbers - 1)
            
            numberOfCurrentScratchCard = numberOfScratchCardsList[scratchCardIndex]

            for currentIndex in range(1, numberOfCommonNumbers + 1):
                winningIndex = scratchCardIndex + currentIndex

                if winningIndex < maximumNumberOfRows:
                    numberOfScratchCardsList[winningIndex] += numberOfCurrentScratchCard 

    numberOfScratchCards = sum(numberOfScratchCardsList) 

    print("Number of Points: " + str(totalPoints))
    print("Number of ScratchCard: " + str(numberOfScratchCards))



            
            
           


if __name__ == '__main__':
    main()
