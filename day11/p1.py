import numpy as np
import sys
from copy import deepcopy

np.set_printoptions(threshold=sys.maxsize)


def main():
    # create universe grid as np 2d-array
    universeGrid = []
    with open('input.txt') as file:
        for line in file:
            row = []
            for char in line:
                if char == '.':
                    row.append(0)
                elif char == '#':
                    row.append(1)
            universeGrid.append(row)
        universeGrid = np.array(universeGrid)

    # expand universe in row direction
    iRow = 0
    while iRow < universeGrid.shape[0]:
        row = universeGrid[iRow,:]
        if np.all(row == 0):
            universeGrid = np.insert(universeGrid, iRow, np.zeros(row.shape), axis=0)
            iRow += 2
        else:
            iRow += 1

    printArr(universeGrid)

    # expand universe in column direction
    iCol = 0
    while iCol < universeGrid.shape[1]:
        column = universeGrid[:,iCol]
        if np.all(column == 0):
            universeGrid = np.insert(universeGrid, iCol, np.zeros(column.shape), axis=1)
            iCol += 2
        else:
            iCol += 1

    galaxies = np.argwhere(universeGrid == 1)
    galaxiesLeft = deepcopy(galaxies)
    distances = []
    for galaxy1 in galaxies:
        galaxiesLeft = galaxiesLeft[1:]
        for galaxy2 in galaxiesLeft:
            distance = abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1])
            distances.append(distance)

    print(sum(distances))


def printArr(arr):
    for i in range(arr.shape[0]):
        row = ''
        for j in range(arr.shape[1]):
            row += str(arr[i,j])
        print(row)
    print('')


if __name__ == '__main__':
    main()