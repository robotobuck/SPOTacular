
def assignAreas(allAreaData):
  optimalRobots = []
  for areaData in allAreaData:
    optimalRobots.append(selectBestFitRobotForArea(areaData))
  return optimalRobots

def selectBestFitRobotForArea(areaData):
  bestIndex = 0
  bestEfficiency = 0
  for i in range(len(areaData)):
    if bestEfficiency < areaData[i]['efficiency']:
      bestIndex = i
      bestEfficiency = areaData[i]['efficiency']
  return bestIndex
