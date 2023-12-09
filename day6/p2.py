import math

time = 49877895
bestDistance = 356137815021882

puzzleAnswer = 1

squareRoot = (-bestDistance + time**2/4)**0.5
upperBound = math.floor(squareRoot + time/2)
lowerBound = math.ceil(-squareRoot + time/2)

puzzleAnswer = (upperBound - lowerBound) + 1

print(puzzleAnswer)