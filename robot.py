import utils


class Robot:
  def __init__(self, robotType):
    self.__robotType = robotType

    self.checkRobotType()

  def displayRobotDetails(self):
    print(f"Robot is of type \'{self.__robotType}\'")

  def checkRobotType(self):
    if self.__robotType not in utils.getRobotTypes():
      self.__robotType = "Unkown"
  
  def getRobotType(self):
    return self.__robotType


class Spot(Robot):
    def __init__(self):
        super().__init__('legged')

class AgileX(Robot):
    def __init__(self):
        super().__init__('wheeled')

class BlueROV2(Robot):
    def __init__(self):
        super().__init__('submarine')

class IntelAero(Robot):
    def __init__(self):
        super().__init__('aerial')