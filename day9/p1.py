def main():
    with open('input.txt') as file:
        puzzleAnswer = 0
        for line in file:
            sequence = [int(nr) for nr in line.split(' ')]
            sequenceEndValues = [sequence[-1]]
            while any(sequence):
                sequence = [sequence[i+1]-sequence[i] for i in range(len(sequence)-1)]
                sequenceEndValues.append(sequence[-1])

            extrapolatedValue = 0
            for endValue in sequenceEndValues:
                extrapolatedValue = endValue + extrapolatedValue

            puzzleAnswer += extrapolatedValue

    print(puzzleAnswer)


if __name__ == '__main__':
    main()