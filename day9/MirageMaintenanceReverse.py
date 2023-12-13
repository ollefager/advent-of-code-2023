import re

def main():
    with open('input.txt', 'r') as file:
        totalSum = 0

        for line in file:
            listValues = list(map(int, re.findall('-?[0-9]+', line)))  # Updated regular expression
            previousValue = obtainPreviousValue(listValues)
            totalSum += previousValue

        print(totalSum)

def obtainPreviousValue(listValues):

    diffValues = [listValues[i] - listValues[i - 1] for i in range(1, len(listValues))]

    if all(diff == 0 for diff in diffValues):
        return listValues[0]
    
    predictionValue     = obtainPreviousValue(diffValues)
    nextPredictionValue = listValues[0] - predictionValue 

    return nextPredictionValue


if __name__ == '__main__':
    main()
