from robot import Robot
from area import AreaToSuvey

# This class finds the ability and efficiency of the robot in the Area given

class RelationshipBetweenRobotAndArea:
  def __init__(self, robot: Robot, area: AreaToSuvey):
    self.__robot = robot
    self.__area = area
    self.__ability = 0 # Max value 10
    self.__efficiency = 0 # Max value 100
    self.findAbilityAndEfficiency()

  def findAbilityAndEfficiency(self):
    if self.__robot.getRobotType() == 'submarine':
      self.submarineAbility()


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
