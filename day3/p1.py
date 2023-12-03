import regex as re

with open('input.txt') as file:
    text = file.read()
    symbols = set(re.findall('[^.0-9]', text))
    file.seek(0)
    textlines = file.readlines()
    sumNumbers = 0
    for iLine, textline in enumerate(textlines):
        numbers = [[m[0], (m.start(0), m.end(0))] for m in re.finditer('[0-9]+', textline)]
        for n in numbers:
            if n[1][0]-1 >= 0:
                s = n[1][0]-1
            else:
                s = n[1][0]
            if n[1][1]+1 < len(textline):
                e = n[1][1]+1
            else:
                e = n[1][1]

            symbolAbove = iLine-1 >= 0 and [char for char in textlines[iLine-1][s:e] if char in symbols]
            symbolBeside = [char for char in [textline[s], textline[e-1]] if char in symbols]
            symbolBelow = iLine+1 < len(textlines) and [char for char in textlines[iLine+1][s:e] if char in symbols]
            if symbolAbove or symbolBeside or symbolBelow:
                print(int(n[0]))
                sumNumbers += int(n[0])
    print(sumNumbers)