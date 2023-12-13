def main():
    with open('input.txt') as file:
        puzzleAnswer = 0
        for line in file:
            sequence = [int(nr) for nr in line.split(' ')]
            sequenceStartValues = [sequence[0]]
            while any(sequence):
                sequence = [sequence[i+1]-sequence[i] for i in range(len(sequence)-1)]
                sequenceStartValues.append(sequence[0])

            extrapolatedValue = 0
            for startValue in reversed(sequenceStartValues):
                extrapolatedValue = startValue - extrapolatedValue

            puzzleAnswer += extrapolatedValue

    print(puzzleAnswer)


if __name__ == '__main__':
    main()