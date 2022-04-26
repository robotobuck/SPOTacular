import random

def generateRandomData (numberOfRobots):
  robotData = []
  for _ in range(numberOfRobots):
    efficiency = random.randrange(100)
    ability = random.randrange(10)
    robotData.append(dict({'efficiency': efficiency, 'ability': ability}))
  return robotData
