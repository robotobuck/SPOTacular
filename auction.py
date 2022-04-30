class Auction:
    """
    Auction class - operates different types of auctions
    """
    BFS = "bfs"
    DFS = "dfs"
    def __init__(self, robots, searchArea):
        self.robots = robots
        self.searchArea = searchArea
        
    def sequentialSingle(self, row, col, type):
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
            return self.__ssBFS(row, col)
        elif type == Auction.DFS:
            return self.__ssDFS(row, col)

    def __ssBFS(self, row, col):
        """
        Sequential Single Bid Auction using Bread First Search for order
        """
        self.__resetGrid()
        order = []  #order of auction

        areas = [self.searchArea[row][col]]  #stack for bfs
        self.searchArea[row][col].visited = True
        while len(areas) > 0:
            current = areas[0]
            current.processed = True
            order.append(current)

            #add new grids if available
            nextRow = current.row
            nextCol = current.col - 1
            if nextCol >= 0 and not self.searchArea[nextRow][nextCol].visited:
                areas.append(self.searchArea[nextRow][nextCol])
                self.searchArea[nextRow][nextCol].visited = True

            nextRow = current.row - 1 
            nextCol = current.col
            if nextRow >= 0 and not self.searchArea[nextRow][nextCol].visited:
                areas.append(self.searchArea[nextRow][nextCol])
                self.searchArea[nextRow][nextCol].visited = True
            
            nextRow = current.row
            nextCol = current.col + 1
            if nextCol < len(self.searchArea[0]) and not self.searchArea[nextRow][nextCol].visited:
                areas.append(self.searchArea[nextRow][nextCol])
                self.searchArea[nextRow][nextCol].visited = True

            nextRow = current.row + 1
            nextCol = current.col
            if nextRow < len(self.searchArea) and not self.searchArea[nextRow][nextCol].visited:
                areas.append(self.searchArea[nextRow][nextCol])
                self.searchArea[nextRow][nextCol].visited = True

            areas.remove(current)

        print('Auction Order: ', [(area.r+str(area.c)) for area in order])
        self.__run(order)

    def __resetGrid(self):
        for row in self.searchArea:
            for area in row:
                area.visited = False
                area.processed = False

    def __run(self, order):
        """
        Execute auction
        """
        print("run auction")

    def __ssDFS(self, row, col):
        """
        Sequential Single Bid Auction using Depth First Search for order
        """
        self.__resetGrid()
        order = []  #order of auction

        areas = [self.searchArea[row][col]]  #stack for bfs
        self.searchArea[row][col].visited = True
        while len(areas) > 0:
            current = areas[len(areas)-1]
            added = False

            #add new grids if available
            nextRow = current.row
            nextCol = current.col - 1
            if nextCol >= 0 and not self.searchArea[nextRow][nextCol].visited:
                added = True
                areas.append(self.searchArea[nextRow][nextCol])
                self.searchArea[nextRow][nextCol].visited = True

            nextRow = current.row - 1 
            nextCol = current.col
            if nextRow >= 0 and not self.searchArea[nextRow][nextCol].visited:
                added = True
                areas.append(self.searchArea[nextRow][nextCol])
                self.searchArea[nextRow][nextCol].visited = True
            
            nextRow = current.row
            nextCol = current.col + 1
            if nextCol < len(self.searchArea[0]) and not self.searchArea[nextRow][nextCol].visited:
                added = True
                areas.append(self.searchArea[nextRow][nextCol])
                self.searchArea[nextRow][nextCol].visited = True

            nextRow = current.row + 1
            nextCol = current.col
            if nextRow < len(self.searchArea) and not self.searchArea[nextRow][nextCol].visited:
                added = True
                areas.append(self.searchArea[nextRow][nextCol])
                self.searchArea[nextRow][nextCol].visited = True

            if not added:   #reached end of grid, begin to process
                current.processed = True
                order.append(current)
                areas.remove(current)

        

        print('Auction Order: ', [(area.r+str(area.c)) for area in order])
        self.__run(order)

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
