import regex as re
import math

def main():

    with open("input.txt", 'r') as file:
        numberList  = []
        numberList2 = []

        for line in file:
            numberList.append([int(num) for num in re.findall('[0-9]+', line)])
            number = ''.join(re.findall('[0-9]+', line))
            numberList2.append(int(number))

        numberOfWinsPerRace = []

        # s = Distance, t = time
        for s,t in zip(numberList[1], numberList[0]):
            numberOfWins = 0
            for t0 in range(1, t):
                if t0 ** 2 - t0*t + s < 0:
                    numberOfWins += 1

            numberOfWinsPerRace.append(numberOfWins)

        numberOfWinsOneRace = 0 
        s = numberList2[1]
        t = numberList2[0]
        for t0 in range(1, t):
            if t0 ** 2 - t0*t + s < 0:
                numberOfWinsOneRace += 1
        
        print(math.prod(numberOfWinsPerRace))
        print(numberOfWinsOneRace)
        
if __name__ == '__main__':
    main()