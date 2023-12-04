import regex as re

with open('input.txt') as file:
    totalPoints = 0
    cards = file.readlines()
    numOfCopiesList = [1]*len(cards)
    for iCard, card in enumerate(cards):
        # get the two sets of numbers of the card
        allNumbers = card.split(':')[1]
        winnningNumbersStr, ownNumbersStr = allNumbers.split('|')
        winningNumbers = re.findall('[0-9]+', winnningNumbersStr)
        ownNumbers = re.findall('[0-9]+', ownNumbersStr)

        # find which numbers are winning numbers
        ownWinningNumbers = [nr for nr in ownNumbers if nr in winningNumbers]

        for i in range(len(ownWinningNumbers)):
            numOfCopiesList[iCard+i+1] += numOfCopiesList[iCard]

    totalNumOfCards = sum(numOfCopiesList)
    print(totalNumOfCards)