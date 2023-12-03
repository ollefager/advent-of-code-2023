import regex as re

wordMap = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
words = list(wordMap.keys())

with open('calibrationDocument.txt') as file:
    textlines = file.readlines()
    sumCalibrationValues = 0
    for textline in textlines:
        wordMatch = re.search('|'.join(words), textline)
        numbers = [[i, c] for i, c in enumerate(textline) if c.isdigit()]
        if wordMatch and numbers:
            matches = []
            for i in range(len(textline)):
                match = re.match('|'.join(words), textline[i:])
                if match:
                    matches.append([i, i + len(match[0])-1, match[0]])

            firstWordMatch = re.search(f"(?<!{'|'.join(words)}){'|'.join(words)}", textline)
            lastWordMatch = re.search(f"{'|'.join(words)}(?!{'|'.join(words)})", textline)
            if matches[0][0] < numbers[0][0]:
                firstDigit = wordMap[matches[0][2]]
            else:
                firstDigit = numbers[0][1]

            if matches[len(matches)-1][1] > numbers[len(numbers)-1][0]:
                lastDigit = wordMap[matches[len(matches)-1][2]]
            else:
                lastDigit = numbers[len(numbers)-1][1]
        elif numbers:
            firstDigit = numbers[0][1]
            lastDigit = numbers[len(numbers) - 1][1]
        elif wordMatch:
            firstDigit = wordMap[firstWordMatch[0]]
            lastDigit = wordMap[lastWordMatch[0]]

        sumCalibrationValues += int(firstDigit + lastDigit)
        print(int(firstDigit + lastDigit))

    print(sumCalibrationValues)