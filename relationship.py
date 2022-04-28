from robot import Robot
from area import AreaToSurvey

# This class finds the ability and efficiency of the robot in the Area given

class RelationshipBetweenRobotAndArea:
  def __init__(self, robot: Robot, area: AreaToSurvey):
    self.__robot = robot
    self.__area = area
    self.__ability = 0 # Max value 10
    self.__efficiency = 0 # Max value 100
    self.findAbilityAndEfficiency()

  def findAbilityAndEfficiency(self):
    if self.__robot.getRobotType() == 'submarine':
      self.submarineAbility()
    if self.__robot.getRobotType() == 'car':
      self.carAbility()
    if self.__robot.getRobotType() == 'drone':
      self.droneAbility()
    if self.__robot.getRobotType() == 'spot':
      self.spotAbility()

  def displayRelationshipInfo(self):
    print(f"Relationship of robot type \'{self.__robot.getRobotType()}\' and \'{self.__area.getEnvironmentType()}\'")
    print(f"Ability: {self.__ability}")
    print(f"Efficiency: {self.__efficiency}")
    
  def submarineAbility(self):
   # Submarine is made to survey water, thus ability and efficiency are maxed out for submarine in water
    if self.__area.getEnvironmentType() == 'water':
        self.__ability = 10
        self.__efficiency = 100
    # Submarine cannot do anything if the area is out of the water, its ability stays at 0

  def carAbility(self):
    env = self.__area.getEnvironmentType()
    if env == 'wooded':
      # The car works best when it can move fast, with trees in the way it is unable to use its full potential
      self.__ability = 7
      self.__efficiency = 40
    if env == 'swamp':
      # The car has to move slower because of hazardous terrain, and can't travel in wet or muddy terrain
      self.__ability = 5
      self.__efficiency = 40
    if env == 'grassy':
      # The car has little to no obstructions, so it can move fast and survey the entire area
      self.__ability = 10
      self.__efficiency = 100
    if env == 'hardpack':
      # The car has limited mobility, but should be able to survey the entire area
      self.__ability = 8
      self.__efficiency = 100
    # If env is unknown or water default to 0 ability and efficiency

  def droneAbility(self):
    env = self.__area.getEnvironmentType()
    if env == 'swamp':
      # The drone should be able to survey swamp entirely from above
      self.__ability = 10
      self.__efficiency = 100
    if env == 'wooded':
      # A drone can move freely above a wooded area, but might not be able to spot or cover too obscured areas
      self.__ability = 10
      self.__efficiency = 85
    if env == 'grassy':
      # The drone should be able to survey a grassy area entirely from above
      self.__ability = 10
      self.__efficiency = 100
    if env == 'hardpack':
      # The drone should be able to survey a grassy area entirely from above
      self.__ability = 10
      self.__efficiency = 100
    # If env is unknown or water default to 0 ability and efficiency

  def spotAbility(self):
    env = self.__area.getEnvironmentType()
    if env == 'swamp':
      # SPOT won't be able to travel at max speed or be able to traverse water in the swamp
      self.__ability = 7
      self.__efficiency = 70
    if env == 'wooded':
      # SPOT won't be able to travel at max speed, but should be able to survey most of the area
      self.__ability = 8
      self.__efficiency = 90
    if env == 'grassy':
      # SPOT will be able to travel at max speed through the entire area
      self.__ability = 10
      self.__efficiency = 100
    if env == 'hardpack':
      # SPOT won't be able to travel at max speed, but should be able to survey most of the area
      self.__ability = 8
      self.__efficiency = 100
    # If env is unknown or water default to 0 ability and efficiency

