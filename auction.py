class Auction:
    """
    Auction class - operates different types of auctions
    """

    BFS = "bfs"
    DFS = "dfs"
    def __init__(self):
        pass
        
    def sequentialSingle(self, robots, searchArea, row, col, type):
        """
        Sequential Single Bid Auction
        @params 
        robots - robot "bidders"
        searchArea - area to search/auction
        row - start row
        col - start column
        type - type of search for auction
        """
        if type == Auction.BFS:
            return self.__ssBFS(searchArea, row, col)
        elif type == Auction.DFS:
            return self.__ssDFS(searchArea, row, col)

    def __ssBFS(self, searchArea, row, col):
        """
        Sequential Single Bid Auction using Bread First Search for order
        """
        self.__resetGrid(searchArea)
        order = []  #order of auction

        areas = [searchArea[row][col]]  #stack for bfs
        searchArea[row][col].visited = True
        while len(areas) > 0:
            current = areas[0]
            current.processed = True
            order.append(current)

            #add new grids if available
            nextRow = current.row
            nextCol = current.col - 1
            if nextCol >= 0 and not searchArea[nextRow][nextCol].visited:
                areas.append(searchArea[nextRow][nextCol])
                searchArea[nextRow][nextCol].visited = True

            nextRow = current.row - 1 
            nextCol = current.col
            if nextRow >= 0 and not searchArea[nextRow][nextCol].visited:
                areas.append(searchArea[nextRow][nextCol])
                searchArea[nextRow][nextCol].visited = True
            
            nextRow = current.row
            nextCol = current.col + 1
            if nextCol < len(searchArea[0]) and not searchArea[nextRow][nextCol].visited:
                areas.append(searchArea[nextRow][nextCol])
                searchArea[nextRow][nextCol].visited = True

            nextRow = current.row + 1
            nextCol = current.col
            if nextRow < len(searchArea) and not searchArea[nextRow][nextCol].visited:
                areas.append(searchArea[nextRow][nextCol])
                searchArea[nextRow][nextCol].visited = True

            areas.remove(current)

        print('Auction Order: ', [(area.r+str(area.c)) for area in order])

    def __resetGrid(self, searchArea):
        for row in searchArea:
            for area in row:
                area.visited = False
                area.processed = False

    def __ssDFS(self, searchArea, row, col):
        """
        Sequential Single Bid Auction using Depth First Search for order
        """
        self.__resetGrid(searchArea)
        order = []  #order of auction

        areas = [searchArea[row][col]]  #stack for bfs
        searchArea[row][col].visited = True
        while len(areas) > 0:
            current = areas[len(areas)-1]
            added = False

            #add new grids if available
            nextRow = current.row
            nextCol = current.col - 1
            if nextCol >= 0 and not searchArea[nextRow][nextCol].visited:
                added = True
                areas.append(searchArea[nextRow][nextCol])
                searchArea[nextRow][nextCol].visited = True

            nextRow = current.row - 1 
            nextCol = current.col
            if nextRow >= 0 and not searchArea[nextRow][nextCol].visited:
                added = True
                areas.append(searchArea[nextRow][nextCol])
                searchArea[nextRow][nextCol].visited = True
            
            nextRow = current.row
            nextCol = current.col + 1
            if nextCol < len(searchArea[0]) and not searchArea[nextRow][nextCol].visited:
                added = True
                areas.append(searchArea[nextRow][nextCol])
                searchArea[nextRow][nextCol].visited = True

            nextRow = current.row + 1
            nextCol = current.col
            if nextRow < len(searchArea) and not searchArea[nextRow][nextCol].visited:
                added = True
                areas.append(searchArea[nextRow][nextCol])
                searchArea[nextRow][nextCol].visited = True

            if not added:   #reached end of grid, begin to process
                current.processed = True
                order.append(current)
                areas.remove(current)

        

        print('Auction Order: ', [(area.r+str(area.c)) for area in order])

    def combinatorial(self, robots, searchArea):
        """
        Combinatorial Bid Auction
        @params 
        robots - robot "bidders"
        searchArea - area to search/auction
        """
        print("Combinatorial")

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
