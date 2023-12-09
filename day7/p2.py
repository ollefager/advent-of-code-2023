cardValueMap = {'A': 14, 'K': 13, 'Q': 12, 'J': 0, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}
handTypeRanks = {'five-of-a-kind':  6,
                 'four-of-a-kind':  5,
                 'full-house':      4,
                 'three-of-a-kind': 3,
                 'two-pair':        2,
                 'one-pair':        1,
                 'high-cards':      0}

def main():
    with open('input.txt') as file:
        hands = {'five-of-a-kind': [],
                 'four-of-a-kind': [],
                 'full-house': [],
                 'three-of-a-kind': [],
                 'two-pair': [],
                 'one-pair': [],
                 'high-cards': []}

        for handInfo in file:
            # parse hand info
            handInfo.replace('\n', '')
            hand, bid = handInfo.split(' ')
            bid = int(bid)

            # get type of hand, if jokers in hand find the best hand type
            jokers = [index for index, card in enumerate(hand) if card == 'J']
            if jokers:
                bestJokerHand, _ = getBestJokerHand(hand, 0, jokers, hand, 0)
                handType = getHandType(bestJokerHand)
            else:
                handType = getHandType(hand)

            # add hand to list corresponding to its type while making sure it stays sorted on hand ranking
            addToSortedHands([hand, bid], hands[handType])

        # concatenate lists of hands to get the final ranking of hands
        sortedHands = []
        for handsOfAType in list(hands.values())[::-1]:
            sortedHands += handsOfAType

        # calculate total winnings from the sorted list of hands
        totalWinnings = 0
        for iHand, hand in enumerate(sortedHands):
            totalWinnings += (iHand + 1)*hand[1]

        print(totalWinnings)


def getHandType(hand):
    # count cards
    cardCount = {}
    for card in hand:
        if card in cardCount.keys():
            cardCount[card] += 1
        else:
            cardCount[card] = 1

    cardCountValues = sorted(list(cardCount.values()), reverse=True)

    if cardCountValues == [5]:
        return 'five-of-a-kind'
    elif cardCountValues == [4, 1]:
        return 'four-of-a-kind'
    elif cardCountValues == [3, 2]:
        return 'full-house'
    elif cardCountValues == [3, 1, 1]:
        return 'three-of-a-kind'
    elif cardCountValues == [2, 2, 1]:
        return 'two-pair'
    elif cardCountValues == [2, 1, 1, 1]:
        return 'one-pair'
    else:
        return 'high-cards'


def addToSortedHands(newHand, hands):
    iSorted = sortHands(newHand, hands, 0)
    hands.insert(iSorted, newHand)


def sortHands(newHand, hands, cardIdx):
    if hands:
        if cardValueMap[hands[len(hands) - 1][0][cardIdx]] < cardValueMap[newHand[0][cardIdx]]:
            iSorted = len(hands)
        else:
            for iHand, hand in enumerate(hands):
                if cardValueMap[hand[0][cardIdx]] == cardValueMap[newHand[0][cardIdx]]:
                    sameHands = [hand]
                    for handSame in hands[iHand+1:]:
                        if cardValueMap[handSame[0][cardIdx]] == cardValueMap[newHand[0][cardIdx]]:
                            sameHands.append(handSame)
                        else:
                            break
                    if cardIdx+1 < len(newHand[0]):
                        iSorted = iHand + sortHands(newHand, sameHands, cardIdx+1)
                    else:
                        iSorted = iHand
                    break
                elif cardValueMap[hand[0][cardIdx]] > cardValueMap[newHand[0][cardIdx]]:
                    iSorted = iHand
                    break
    else:
        iSorted = 0

    return iSorted


def getBestJokerHand(hand, jokerIdx, jokers, bestJokerHand, bestJokerHandRank):
    for card in cardValueMap.keys():
        jokerHand = hand[:jokers[jokerIdx]] + card + hand[jokers[jokerIdx] + 1:]
        if jokerIdx < len(jokers)-1:
            bestJokerHand, bestJokerHandRank = getBestJokerHand(jokerHand, jokerIdx + 1, jokers, bestJokerHand, bestJokerHandRank)
        else:
            jokerHandType = getHandType(jokerHand)
            jokerHandRank = handTypeRanks[jokerHandType]
            if jokerHandRank > bestJokerHandRank:
                bestJokerHand = jokerHand
                bestJokerHandRank = jokerHandRank

    return bestJokerHand, bestJokerHandRank






if __name__ == '__main__':
    main()