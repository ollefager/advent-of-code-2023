raceTimes = [49, 87, 78, 95]
bestDistances = [356, 1378, 1502, 1882]

puzzleAnswer = 1

for iRace in range(len(raceTimes)):
    time = raceTimes[iRace]
    bestDistance = bestDistances[iRace]

    numOfRecordBeatingDistances = 0
    for buttonTime in range(1, time):
        raceDistance = (time - buttonTime)*buttonTime
        if raceDistance > bestDistance:
            numOfRecordBeatingDistances += 1

    puzzleAnswer *= numOfRecordBeatingDistances

print(puzzleAnswer)
