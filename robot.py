import utils


class Robot:
    def __init__(self, robotType, maxAreas):
        self.__robotType = robotType
        self.maxAreas = maxAreas
        self.areaAssignments = []

        self.checkRobotType()

    def assignArea(self, area):
        self.areaAssignments.append(area)
        
    def displayRobotDetails(self):
        print(f"Robot is of type \'{self.__robotType}\'")

    def checkRobotType(self):
        if self.__robotType not in utils.getRobotTypes():
            self.__robotType = "Unkown"
  
    def getRobotType(self):
        return self.__robotType


class Spot(Robot):
    def __init__(self, startRow, startCol):
        """
        init
        @params
        startRow, startCol - start coordinates of robot
        """
        super().__init__('legged', 4)
        self.row = startRow
        self.col = startCol
        self.maxTravel = 4

    def bidSingle(self, area, row, col):
        """
        Single Bid
        @params
        area - search area
        row, col - current area for bid
        """
        bid = -1
        distanceToArea = abs(self.row - row) + abs(self.col - col)
        # Only bid if the area is close enough
        if distanceToArea <= self.maxTravel:
            bid = ((self.maxTravel - distanceToArea) / self.maxTravel) * (100 * (self.maxAreas - len(self.areaAssignments)) / self.maxAreas)
        return bid

class AgileX(Robot):
    def __init__(self, startRow, startCol):
        """
        init
        @params
        startRow, startCol - start coordinates of robot
        """
        super().__init__('wheeled', 6)
        self.row = startRow
        self.col = startCol
        self.maxTravel = 5

    def bidSingle(self, area, row, col):
        """
        Single Bid
        @params
        area - search area
        row, col - current area for bid
        """
        bid = -1
        distanceToArea = abs(self.row - row) + abs(self.col - col)
        # Only bid if the area is close enough
        if distanceToArea <= self.maxTravel:
            bid = ((self.maxTravel - distanceToArea) / self.maxTravel) * (100 * (self.maxAreas - len(self.areaAssignments)) / self.maxAreas)
        return bid

class BlueROV2(Robot):
    def __init__(self, startRow, startCol):
        """
        init
        @params
        startRow, startCol - start coordinates of robot
        """
        super().__init__('submarine', 2)
        self.row = startRow
        self.col = startCol
        self.maxTravel = 2

    def bidSingle(self, area, row, col):
        """
        Single Bid
        @params
        area - search area
        row, col - current area for bid
        """
        bid = -1
        distanceToArea = abs(self.row - row) + abs(self.col - col)
        # Only bid if the area is close enough
        if distanceToArea <= self.maxTravel:
            bid = ((self.maxTravel - distanceToArea) / self.maxTravel) * (100 * (self.maxAreas - len(self.areaAssignments)) / self.maxAreas)
        return bid

class IntelAero(Robot):
    def __init__(self, startRow, startCol):
        """
        init
        @params
        startRow, startCol - start coordinates of robot
        """
        super().__init__('legged', 8)
        self.row = startRow
        self.col = startCol
        self.maxTravel = 6

    def bidSingle(self, area, row, col):
        """
        Single Bid
        @params
        area - search area
        row, col - current area for bid
        """
        bid = -1
        distanceToArea = abs(self.row - row) + abs(self.col - col)
        # Only bid if the area is close enough
        if distanceToArea <= self.maxTravel:
            bid = ((self.maxTravel - distanceToArea) / self.maxTravel) * (100 * (self.maxAreas - len(self.areaAssignments)) / self.maxAreas)
        return bid