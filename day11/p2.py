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

    emptyRows = np.array([iRow for iRow, row in enumerate(np.all(universeGrid == np.zeros((universeGrid.shape[0], 1)), axis=1)) if row])
    emptyCols = np.array([iCol for iCol, col in enumerate(np.all(universeGrid == np.zeros((1, universeGrid.shape[1])), axis=0)) if col])

    galaxies = np.argwhere(universeGrid == 1)
    galaxiesLeft = deepcopy(galaxies)
    distances = []
    for galaxy1 in galaxies:
        galaxiesLeft = galaxiesLeft[1:]
        for galaxy2 in galaxiesLeft:
            nEmptyRowsBetweenGalaxies = sum((min(galaxy1[0], galaxy2[0]) < emptyRows) & (emptyRows  < max(galaxy1[0], galaxy2[0])))
            nEmptyColsBetweenGalaxies = sum((min(galaxy1[1], galaxy2[1]) < emptyCols) & (emptyCols < max(galaxy1[1], galaxy2[1])))
            distance = abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1])
            expandedDistance = distance + (nEmptyRowsBetweenGalaxies + nEmptyColsBetweenGalaxies)*(1000000-1)
            distances.append(expandedDistance)

    print(sum(distances))
    

if __name__ == '__main__':
    main()