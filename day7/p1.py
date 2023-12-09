cardValueMap = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}


def main():
    with open('input.txt') as file:
        fiveOfAKindHands = []
        fourOfAKindHands = []
        fullHouseHands = []
        threeOfAKindHands = []
        twoPairHands = []
        onePairHands = []
        highCardHands = []
        for handInfo in file:
            handInfo.replace('\n', '')
            hand, bid = handInfo.split(' ')
            bid = int(bid)

            # count cards
            cardCount = {}
            for card in hand:
                if card in cardCount.keys():
                    cardCount[card] += 1
                else:
                    cardCount[card] = 1

            cardCountValues = sorted(list(cardCount.values()), reverse=True)
            if cardCountValues == [5]:
                addToSortedHands([hand, bid], fiveOfAKindHands)
            elif cardCountValues == [4,1]:
                addToSortedHands([hand, bid], fourOfAKindHands)
            elif cardCountValues == [3, 2]:
                addToSortedHands([hand, bid], fullHouseHands)
            elif cardCountValues == [3,1,1]:
                addToSortedHands([hand, bid], threeOfAKindHands)
            elif cardCountValues == [2,2,1]:
                addToSortedHands([hand, bid], twoPairHands)
            elif cardCountValues == [2,1,1,1]:
                addToSortedHands([hand, bid], onePairHands)
            else:
                addToSortedHands([hand, bid], highCardHands)

        sortedHands = highCardHands + onePairHands + twoPairHands + threeOfAKindHands + fullHouseHands + fourOfAKindHands + fiveOfAKindHands

        totalWinnings = 0
        for iHand, hand in enumerate(sortedHands):
            totalWinnings += (iHand + 1)*hand[1]

        print(totalWinnings)


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


if __name__ == '__main__':
    main()