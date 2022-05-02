from area import AreaToSurvey
import math

class Robot:
    def __init__(self, robotType, start, maxTravel):
        self.__robotType = robotType
        self.start = start
        self.maxTravel = maxTravel
        self.reset()

    def reset(self):
        self.position = self.start
        self.travelLeft = self.maxTravel
        self.areaAssignments = []

    def assignArea(self, area):
        distanceToArea = math.sqrt((self.position['x'] - area.center['x'])*(self.position['x'] - area.center['x']) + (self.position['y'] - area.center['y'])*(self.position['y'] - area.center['y']))
        areaOfArea = area.getSurfaceArea()
        dist = distanceToArea + areaOfArea

        self.areaAssignments.append(area)
        self.travelLeft -= dist         #used some travel
        self.position = area.center     #move robot to new location
        
    def displayRobotDetails(self):
        print(f"Robot is of type \'{self.__robotType}\'")
  
    def getRobotType(self):
        return self.__robotType


class Spot(Robot):
    def __init__(self, start):
        """
        init
        @params
        start - start coordinates of robot (x,y)
        """
        super().__init__('legged', start, 10800)

        self.powerPerMeter = 2
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
            e = area.getEnvironmentType()
            bid *= self.terrainEffectiveness[area.getEnvironmentType()] #use effectiveness term

        # if limited by distance (battery charge)
        if limitByDistance: 
            if dist > self.travelLeft:
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
        super().__init__('wheeled', start, 12000)

        self.powerPerMeter = 3
        self.terrainEffectiveness = { 'water':0, 'wooded':.75, 'grassy':1, 'rocky':0 }

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
            if dist > self.travelLeft:
                bid = 0

        return bid

class BlueROV2(Robot):
    def __init__(self, start):
        """
        init
        @params
        startRow, startCol - start coordinates of robot
        """
        super().__init__('submarine', start, 5400)

        self.powerPerMeter = 2.5
        self.terrainEffectiveness = { 'water':1, 'wooded':0, 'grassy':0, 'rocky':0 }

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
            if dist > self.travelLeft:
                bid = 0

        return bid

class IntelAero(Robot):
    def __init__(self, start):
        """
        init
        @params
        startRow, startCol - start coordinates of robot
        """
        super().__init__('aerial', start, 18000)

        self.powerPerMeter = 1
        self.terrainEffectiveness = { 'water':.33, 'wooded':.5, 'grassy':1, 'rocky':1 }

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
            if dist > self.travelLeft:
                bid = 0

        return bid