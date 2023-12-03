import regex as re

with open('input.txt') as file:
    text = file.read()
    symbols = set(re.findall('[^.0-9]', text))
    file.seek(0)
    textlines = file.readlines()
    sumNumbers = 0
    gearMatrix = [[None for i in range(len(textlines[0]))] for j in range(len(textlines))]
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

            gearIndices = []
            if iLine-1 >= 0:
                gearIndices += [[iLine-1, s+iChar] for iChar, char in enumerate(textlines[iLine-1][s:e]) if char == '*']

            gearIndices += [[iLine, s*(abs(iChar-1))+(e-1)*iChar] for iChar, char in enumerate([textline[s], textline[e-1]]) if char == '*']

            if iLine+1 < len(textlines):
                gearIndices += [[iLine+1, s+iChar] for iChar, char in enumerate(textlines[iLine + 1][s:e]) if char == '*']

            for gearIndex in gearIndices:
                if gearMatrix[gearIndex[0]][gearIndex[1]] is None:
                    gearMatrix[gearIndex[0]][gearIndex[1]] = [int(n[0])]
                else:
                    gearMatrix[gearIndex[0]][gearIndex[1]].append(int(n[0]))

    for row in gearMatrix:
        for element in row:
            if element is not None and len(element) == 2:
                sumNumbers += element[0]*element[1]

    print(sumNumbers)