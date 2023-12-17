from copy import deepcopy
import numpy as np

pipeDirectionsMap = {'|': np.array([[1,0], [-1,0]]),
                     '-': np.array([[0,-1], [0,1]]),
                     'L': np.array([[-1,0], [0,1]]),
                     'J': np.array([[0,-1], [-1,0]]),
                     '7': np.array([[1,0], [0,-1]]),
                     'F': np.array([[1,0], [0,1]])}


def main():
    with open('input.txt') as file:
        # extract grid from inpt
        grid = [list(line) for line in file]

        # find start position
        for iRow, row in enumerate(grid):
            for iTile, tile in enumerate(row):
                if tile == 'S':
                    start = np.array([iRow, iTile])
                    break

        # find the neighbour pipes connected to start tile
        pipeContinuations = []
        for neighbour in np.array([[1,0], [-1,0], [0,1], [0,-1]]):
            neighbourCoordinates = start+neighbour
            neighbourPipeType = grid[neighbourCoordinates[0]][neighbourCoordinates[1]]
            if np.any(np.all(pipeDirectionsMap[neighbourPipeType] == -neighbour, axis=1)):
                pipeContinuations.append([start+neighbour, neighbourPipeType])

        # add start pipe to map
        pipeDirectionsMap['S'] = np.array([pipeContinuations[0][0] - start, pipeContinuations[1][0] - start])

        # get pipes in loop
        forwardPipe = pipeContinuations[0]
        prevForwardPipe = [start, 'S']
        pipesInLoop = [forwardPipe[0]]
        step = 0
        while forwardPipe[1] != 'S':
            entranceDir = prevForwardPipe[0] - forwardPipe[0]
            exitDir = [direction for direction in pipeDirectionsMap[forwardPipe[1]] if np.any(direction != entranceDir)]
            prevForwardPipe = deepcopy(forwardPipe)
            pipeType = grid[forwardPipe[0][0]+exitDir[0][0]][forwardPipe[0][1]+exitDir[0][1]]
            forwardPipe = [forwardPipe[0]+exitDir[0], pipeType]

            pipesInLoop.append(forwardPipe[0])
            step += 1

        # # print loop
        # loopGrid = f''
        # for iRow, row in enumerate(grid):
        #     print(iRow)
        #     for iTile, tile in enumerate(row):
        #         if np.any(np.all(np.array([iRow, iTile]) == pipesInLoop, axis=1)):
        #             loopGrid += tile
        #         else:
        #             loopGrid += '.'
        #     loopGrid += '\n'
        # print(loopGrid)

        # find enclosed tiles
        downDir = np.array([1, 0])
        enclosedTiles = []
        for iCol in range(len(grid[0])):
            print(iCol)
            foundFirstLoopTile = False
            foundFirstCrossing = False
            for iRow in range(len(grid)):
                tile = np.array([iRow, iCol])
                tileInLoop = np.any(np.all(tile == pipesInLoop, axis=1))

                if tileInLoop and not foundFirstLoopTile:
                    foundFirstLoopTile = True
                    enclosingTiles = checkIfEnclosingTiles(downDir, tile, pipesInLoop, grid)
                elif tileInLoop:
                    pipeDirections = pipeDirectionsMap[grid[tile[0]][tile[1]]]
                    pipeConnectedToPrevious = np.any(np.all(-downDir == pipeDirections, axis=1))
                    pipeConnectedToNext = np.any(np.all(downDir == pipeDirections, axis=1))
                    if not pipeConnectedToPrevious and not pipeConnectedToNext:
                        enclosingTiles = not enclosingTiles
                        foundFirstCrossing = True
                    elif not pipeConnectedToPrevious and pipeConnectedToNext:
                        crossingInDir = pipeDirections[np.all(downDir != pipeDirections, axis=1)]
                        foundFirstCrossing = True
                    elif pipeConnectedToPrevious and not pipeConnectedToNext:
                        crossingOutDir = pipeDirections[np.all(-downDir != pipeDirections, axis=1)]
                        if foundFirstCrossing and not np.all(crossingInDir == crossingOutDir):
                            enclosingTiles = not enclosingTiles
                elif foundFirstLoopTile:
                    if enclosingTiles and (not enclosedTiles or not np.any(np.all(tile == enclosedTiles, axis=1))):
                        enclosedTiles.append(deepcopy(tile))
                        #loopGridIdx = (len(grid[0]) + 1) * tile[0] + tile[1]
                        #print(loopGrid[loopGridIdx])
                        #loopGrid = loopGrid[:loopGridIdx] + 'I' + loopGrid[loopGridIdx + 1:]

        #print(loopGrid)
        print(len(enclosedTiles))


def checkIfEnclosingTiles(direction, startTile, pipesInLoop, grid):
    nextTile = startTile + direction
    foundFirstCrossing = False
    nCrossings = 0
    while 0 < nextTile[0] < len(grid) and 0 < nextTile[1] < len(grid[0]):
        pipeInLoop = np.any(np.all(nextTile == pipesInLoop, axis=1))
        if pipeInLoop:
            pipeDirections = pipeDirectionsMap[grid[nextTile[0]][nextTile[1]]]
            pipeConnectedToPrevious = np.any(np.all(-direction == pipeDirections, axis=1))
            pipeConnectedToNext = np.any(np.all(direction == pipeDirections, axis=1))
            if not pipeConnectedToPrevious and not pipeConnectedToNext:
                nCrossings += 1
                foundFirstCrossing = True
            elif not pipeConnectedToPrevious and pipeConnectedToNext:
                crossingInDir = pipeDirections[np.all(direction != pipeDirections, axis=1)]
                foundFirstCrossing = True
            elif pipeConnectedToPrevious and not pipeConnectedToNext:
                crossingOutDir = pipeDirections[np.all(-direction != pipeDirections, axis=1)]
                if foundFirstCrossing and not np.all(crossingInDir == crossingOutDir):
                    nCrossings += 1

        nextTile += direction

    enclosingTiles = nCrossings % 2 != 0

    return enclosingTiles


if __name__ == '__main__':
    main()

