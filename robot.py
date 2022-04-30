import utils


class Robot:
    def __init__(self, robotType, maxAreas):
        self.__robotType = robotType
        self.__maxAreas = maxAreas
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

    def bidSingle(self, area, row, col):
        """
        Single Bid
        @params
        area - search area
        row, col - current area for bid
        """
        return 0

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

    def bidSingle(self, area, row, col):
        """
        Single Bid
        @params
        area - search area
        row, col - current area for bid
        """
        return 0

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

    def bidSingle(self, area, row, col):
        """
        Single Bid
        @params
        area - search area
        row, col - current area for bid
        """
        return 0

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

    def bidSingle(self, area, row, col):
        """
        Single Bid
        @params
        area - search area
        row, col - current area for bid
        """
        return 0