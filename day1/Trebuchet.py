def main():
    sum = 0
    conversionMap = {"one": "o1e", "two": "t2o", "three": "t3e", "four": "f4r", "five": "f5e",
                     "six": "s6x", "seven": "s7n", "eight": "e8t", "nine": "n9e", "zero": "z2o"}
    
    with open('input.txt', 'r') as file:
        for string in file:
            string = replaceSubstringsWithDigits(string, conversionMap) # Comment to get solution for part 1

            digits = ''.join(char for char in string if char.isdigit())
            partSum = int(digits[0] + digits[-1])

            sum += partSum
    print(sum)

def replaceSubstringsWithDigits(string, replacements):
    for substring, replaceString in replacements.items():
        string = string.replace(substring, replaceString)
    return string
    
if __name__ == '__main__':
    main()



