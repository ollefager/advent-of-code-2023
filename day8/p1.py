import regex as re

with open('input.txt') as file:
    lines = file.readlines()
    lrSequence = lines[0].replace('\n', '')

    # create node map
    nodeMap = {}
    for line in lines[2:]:
        nodes = re.findall('[A-Z]{3}', line)
        nodeMap[nodes[0]] = {'L': nodes[1], 'R': nodes[2]}

    node = 'AAA'
    steps = 0
    while node != 'ZZZ':
        for direction in lrSequence:
            node = nodeMap[node][direction]
            steps += 1
            if node == 'ZZZ':
                break

    print(steps)