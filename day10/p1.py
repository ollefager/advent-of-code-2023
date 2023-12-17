from copy import deepcopy
import numpy as np

base = np.array([0,0])
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

        pipeContinuations = []
        for neighbour in np.array([[1,0], [-1,0], [0,1], [0,-1]]):
            neighbourCoordinates = start+neighbour
            neighbourPipeType = grid[neighbourCoordinates[0]][neighbourCoordinates[1]]
            if np.any(np.all(pipeDirectionsMap[neighbourPipeType] == -neighbour, axis=1)):
                pipeContinuations.append([start+neighbour, neighbourPipeType])

        forwardPipe = pipeContinuations[0]
        backwardPipe = pipeContinuations[1]
        prevForwardPipe = [start, 'S']
        prevBackwardPipe = [start, 'S']
        steps = 1
        while np.any(forwardPipe[0] != backwardPipe[0]):
            entranceDir = prevForwardPipe[0] - forwardPipe[0]
            exitDir = [direction for direction in pipeDirectionsMap[forwardPipe[1]] if np.any(direction != entranceDir)]
            prevForwardPipe = deepcopy(forwardPipe)
            pipeType = grid[forwardPipe[0][0]+exitDir[0][0]][forwardPipe[0][1]+exitDir[0][1]]
            forwardPipe = [forwardPipe[0]+exitDir[0], pipeType]
            print(forwardPipe)

            entranceDir = prevBackwardPipe[0] - backwardPipe[0]
            exitDir = [direction for direction in pipeDirectionsMap[backwardPipe[1]] if np.any(direction != entranceDir)]
            prevBackwardPipe = deepcopy(backwardPipe)
            pipeType = grid[backwardPipe[0][0] + exitDir[0][0]][backwardPipe[0][1] + exitDir[0][1]]
            backwardPipe = [backwardPipe[0]+exitDir[0], pipeType]
            print(backwardPipe)
            print()

            steps += 1

        print(steps)


if __name__ == '__main__':
    main()

