import regex as re

with open('input.txt') as file:
    lines = file.readlines()
    lrSequence = lines[0].replace('\n', '')

    # create node map and get start nodes
    nodeMap = {}
    startNodes = []
    for line in lines[2:]:
        nodes = re.findall('[A-Z]{3}', line)
        nodeMap[nodes[0]] = {'L': nodes[1], 'R': nodes[2]}

        if nodes[0][2] == 'A':
            startNodes.append(nodes[0])

    nodes = startNodes
    steps = 0
    reachedEnd = False
    while not reachedEnd:
        for direction in lrSequence:
            reachedEnd = True
            nodesReachedEnd = []
            for iNode, node in enumerate(nodes):
                newNode = nodeMap[node][direction]
                nodes[iNode] = newNode
                if newNode[2] != 'Z':
                    reachedEnd = False
                else:
                    nodesReachedEnd.append(newNode)
            if len(nodesReachedEnd) > 2:
                print(nodesReachedEnd, steps)
            steps += 1
            if reachedEnd:
                break

    print(steps)