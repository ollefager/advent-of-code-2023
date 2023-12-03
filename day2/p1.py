import regex as re

content = {'red': 12, 'green': 13, 'blue': 14}

with open('input.txt') as file:
    games = file.readlines()
    sumGames = 0
    for iGame, game in enumerate(games):
        gamePossible = True
        _, gameInfo = game.split(':')
        draws = gameInfo.split(';')
        for draw in draws:
            colorInfos = draw.split(',')
            for colorInfo in colorInfos:
                color = re.search('[a-z]+', colorInfo)[0]
                numOfCubes = int(re.search('[0-9]+', colorInfo)[0])
                if numOfCubes > content[color]:
                    gamePossible = False

        if gamePossible:
            sumGames += iGame+1

    print(sumGames)