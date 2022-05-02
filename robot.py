import utils
from area import AreaToSurvey
import math

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
    def __init__(self, start):
        """
        init
        @params
        start - start coordinates of robot (x,y)
        """
        super().__init__('legged', 4)
        self.start = start
        self.position = start
        self.powerPerMeter = 2
        self.maxTravel = 10800

        self.terrainEffectiveness = { 'water':0, 'wooded':1, 'grassy':1, 'rocky':1 }

    def bidSingle(self, area:list, limitByDistance:bool, limitByTerrain:bool):
        """
        Single Bid
        @params
        area - search area
        row, col - current area for bid
        limitByDistance - limit bidding by max distance?
        limitByTerrain - limit bidding by terrain?
        """
        bid = 0
        distanceToArea = math.sqrt((self.position['x'] - area.center['x'])*(self.position['x'] - area.center['x']) + (self.position['y'] - area.center['y'])*(self.position['y'] - area.center['y']))
        areaOfArea = area.getSurfaceArea()
        dist = distanceToArea + areaOfArea
        powerConsumption = (distanceToArea + areaOfArea) * self.powerPerMeter

        bid = 1/powerConsumption
        # if limited by terrain type
        if limitByTerrain:
            bid *= self.terrainEffectiveness[area.getEnvironmentType()] #use effectiveness term

        # if limited by distance (battery charge)
        if limitByDistance: 
            if dist > self.maxTravel:
                bid = 0

        return bid

    def awardBid(self, area:AreaToSurvey, row, col):
        """
        """
        pass


class AgileX(Robot):
    def __init__(self, start):
        """
        init
        @params
        startRow, startCol - start coordinates of robot
        """
        super().__init__('wheeled', 6)
        self.start = start
        self.position = start
        self.powerPerMeter = 3
        self.maxTravel = 32400

    def bidSingle(self, area:list, limitByDistance:bool, limitByTerrain:bool):
        """
        Single Bid
        @params
        area - search area
        row, col - current area for bid
        limitByDistance - limit bidding by max distance?
        limitByTerrain - limit bidding by terrain?
        """
        bid = 0
        distanceToArea = math.sqrt((self.position['x'] - area.center['x'])*(self.position['x'] - area.center['x']) + (self.position['y'] - area.center['y'])*(self.position['y'] - area.center['y']))
        areaOfArea = area.getSurfaceArea()
        dist = distanceToArea + areaOfArea
        powerConsumption = (distanceToArea + areaOfArea) * self.powerPerMeter

        bid = 1/powerConsumption
        # if limited by terrain type
        if limitByTerrain:
            bid *= self.terrainEffectiveness[area.getEnvironmentType()] #use effectiveness term

        # if limited by distance (battery charge)
        if limitByDistance: 
            if dist > self.maxTravel:
                bid = 0

        return bid

class BlueROV2(Robot):
    def __init__(self, start):
        """
        init
        @params
        startRow, startCol - start coordinates of robot
        """
        super().__init__('submarine', 2)
        self.start = start
        self.position = start
        self.powerPerMeter = 2.5
        self.maxTravel = 5400

    def bidSingle(self, area:list, limitByDistance:bool, limitByTerrain:bool):
        """
        Single Bid
        @params
        area - search area
        row, col - current area for bid
        limitByDistance - limit bidding by max distance?
        limitByTerrain - limit bidding by terrain?
        """
        bid = 0
        distanceToArea = math.sqrt((self.position['x'] - area.center['x'])*(self.position['x'] - area.center['x']) + (self.position['y'] - area.center['y'])*(self.position['y'] - area.center['y']))
        areaOfArea = area.getSurfaceArea()
        dist = distanceToArea + areaOfArea
        powerConsumption = (distanceToArea + areaOfArea) * self.powerPerMeter

        bid = 1/powerConsumption
        # if limited by terrain type
        if limitByTerrain:
            bid *= self.terrainEffectiveness[area.getEnvironmentType()] #use effectiveness term

        # if limited by distance (battery charge)
        if limitByDistance: 
            if dist > self.maxTravel:
                bid = 0

        return bid

class IntelAero(Robot):
    def __init__(self, start):
        """
        init
        @params
        startRow, startCol - start coordinates of robot
        """
        super().__init__('aerial', 8)
        self.start = start
        self.position = start
        self.powerPerMeter = 1
        self.maxTravel = 64800

    def bidSingle(self, area:list, limitByDistance:bool, limitByTerrain:bool):
        """
        Single Bid
        @params
        area - search area
        row, col - current area for bid
        limitByDistance - limit bidding by max distance?
        limitByTerrain - limit bidding by terrain?
        """
        bid = 0
        distanceToArea = math.sqrt((self.position['x'] - area.center['x'])*(self.position['x'] - area.center['x']) + (self.position['y'] - area.center['y'])*(self.position['y'] - area.center['y']))
        areaOfArea = area.getSurfaceArea()
        dist = distanceToArea + areaOfArea
        powerConsumption = (distanceToArea + areaOfArea) * self.powerPerMeter

        bid = 1/powerConsumption
        # if limited by terrain type
        if limitByTerrain:
            bid *= self.terrainEffectiveness[area.getEnvironmentType()] #use effectiveness term

        # if limited by distance (battery charge)
        if limitByDistance: 
            if dist > self.maxTravel:
                bid = 0

        return bid