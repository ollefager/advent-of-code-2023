with open('input.txt') as file:
    textlines = file.readlines()
    sumCalibrationValues = 0
    for textline in textlines:
        numbers = [c for c in textline if c.isdigit()]
        if len(numbers) == 1:
            sumCalibrationValues += int(numbers[0] + numbers[0])
        else:
            sumCalibrationValues += int(numbers[0] + numbers[len(numbers)-1])

    print(sumCalibrationValues)
