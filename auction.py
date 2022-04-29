class Auction:
    BFS = "bfs"
    DFS = "dfs"
    def __init__(self):
        pass

    def sequentialSingle(self, searchArea, type):
        if type == Auction.BFS:
            return self.__ssBFS(searchArea)
        elif type == Auction.DFS:
            return self.__ssDFS(searchArea)

    def __ssBFS(self, searchArea):
        return "BFS"

    def __ssDFS(self, searchArea):
        return "DFS"

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
