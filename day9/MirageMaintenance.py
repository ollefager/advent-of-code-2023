import re

def main():
    with open('input.txt', 'r') as file:
        totalSum = 0

        for line in file:
            listValues = list(map(int, re.findall('-?[0-9]+', line)))  # Updated regular expression
            predictionValue = obtainPrediction(listValues)
            totalSum += predictionValue

        print(totalSum)

def obtainPrediction(listValues):

    diffValues = [listValues[i] - listValues[i - 1] for i in range(1, len(listValues))]

    if all(diff == 0 for diff in diffValues):
        return listValues[0]
    
    predictionValue     = obtainPrediction(diffValues)

    nextPredictionValue = listValues[-1] + predictionValue # Part 1
    #nextPredictionValue = listValues[0] - predictionValue # Part 2

    return nextPredictionValue


if __name__ == '__main__':
    main()
