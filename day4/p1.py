import regex as re

with open('input.txt') as file:
    totalPoints = 0
    for card in file:
        # get the two sets of numbers of the card
        allNumbers = card.split(':')[1]
        winnningNumbersStr, ownNumbersStr = allNumbers.split('|')
        winningNumbers = re.findall('[0-9]+', winnningNumbersStr)
        ownNumbers = re.findall('[0-9]+', ownNumbersStr)

        # find which numbers are winning numbers
        ownWinningNumbers = [nr for nr in ownNumbers if nr in winningNumbers]

        numOfWinningNumbers = len(ownWinningNumbers)
        points = 2**(numOfWinningNumbers-1)*(numOfWinningNumbers > 0) # need to set points to 0 if no winning numbers
        totalPoints += points

    print(totalPoints)
