from area import AreaToSurvey
from robot import Robot


class Auction:
    """
    Auction class - operates different types of auctions
    """
    BFS = "bfs"
    DFS = "dfs"
    def __init__(self, robots: Robot, searchArea: AreaToSurvey):
        self.robots = robots
        self.searchArea = searchArea
        
    def sequentialSingle(self, row, col, type, limitByDistance, limitByTerrain):
        """
        Sequential Single Bid Auction
        @params 
        robots - robot "bidders"
        searchArea - area to search/auction
        row - start row
        col - start column
        type - type of search for auction
        limitByDistance - limit bidding by max distance?
        limitByTerrain - limit bidding by terrain?
        """

        for bot in self.robots:
            bot.reset()

        if type == Auction.BFS:
            return self.__ssBFS(row, col, limitByDistance, limitByTerrain)
        elif type == Auction.DFS:
            return self.__ssDFS(row, col, limitByDistance, limitByTerrain)

    def __ssBFS(self, row, col, limitByDistance, limitByTerrain):
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
        self.__run(order, limitByDistance, limitByTerrain)

    def __resetGrid(self):
        for row in self.searchArea:
            for area in row:
                area.visited = False
                area.processed = False

    def __run(self, order, limitByDistance, limitByTerrain):
        """
        Execute auction
        """
        for area in order:
            bids = []
            winningBot = 0
            winningBid = 0
            for bot in self.robots:
                botBid = bot.bidSingle(area, limitByDistance, limitByTerrain)
                bids.append(botBid)
                if botBid > winningBid:
                    winningBot = bot
                    winningBid = botBid
            if winningBid > 0:
                winningBot.assignArea(area)
            # If no bid > 0 no robot can survery the area
        for bot in self.robots:
            print(f"Robot type \"{bot.getRobotType()}\" assigned to survey {len(bot.areaAssignments)} areas: ", [(area.r + str(area.c)) for area in bot.areaAssignments])

    def __resetRobots(self):
        for bot in self.robots:
            bot.areaAssignments = []

    def __ssDFS(self, row, col, limitByDistance, limitByTerrain):
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
        self.__run(order, limitByDistance, limitByTerrain)
