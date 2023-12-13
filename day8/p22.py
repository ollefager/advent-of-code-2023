import regex as re
import numpy as np

with open('input.txt') as file:
    lines = file.readlines()
    lrSequence = lines[0].replace('\n', '')

    # create node map and get start nodes
    nodeMap = {}
    startNodes = []
    endNodes = []
    for iLine, line in enumerate(lines[2:]):
        nodes = re.findall('[A-Z]{3}', line)
        nodeMap[nodes[0]] = {'L': nodes[1], 'R': nodes[2], 'i': iLine}

        if nodes[0][2] == 'A':
            startNodes.append(nodes[0])
        elif nodes[0][2] == 'Z':
            endNodes.append(nodes[0])

    bigNodeMap = {}
    for node in nodeMap.keys():
        subSequenceMap = {}
        for iDirection in range(len(lrSequence)):
            subSequence = lrSequence[:iDirection+1]
            endNode = node
            for direction in subSequence:
                endNode = nodeMap[endNode][direction]

            subSequenceMap[subSequence] = endNode

        bigNodeMap[node] = subSequenceMap

    # mapMatrix = []
    # for node in nodeMap.keys():
    #     mapMatrix.append([nodeMap[nodeMap[node]['L']]['i'],
    #                       nodeMap[nodeMap[node]['R']]['i'],
    #                       2 if node in endNodes else 1])
    # np.array(mapMatrix)

    nodes = startNodes
    steps = 0
    endReached = False
    while not endReached:
        for iDir in range(len(lrSequence)):
            direction = lrSequence[iDir]
            firstNodeReachedEnd = False
            endReached = True
            nodesReachedEnd = []

            newNode = nodeMap[nodes[0]][direction]
            nodes[0] = newNode
            steps += 1
            if newNode[2] == 'Z':
                firstNodeReachedEnd = True

                nodesReachedEnd = [newNode]
                for node in nodes[1:]:
                    newNode = bigNodeMap[node][lrSequence[:iDir+1]]
                    if newNode[2] != 'Z':
                        endReached = False
                        break
                    else:
                        nodesReachedEnd.append(newNode)

                if len(nodesReachedEnd) > 2:
                    print(nodesReachedEnd, steps)
            else:
                endReached = False

            if endReached:
                break

            if iDir == len(lrSequence)-1:
                for iNode in range(1,len(nodes)):
                     nodes[iNode] = bigNodeMap[nodes[iNode]][lrSequence[:iDir+1]]

    print(steps)