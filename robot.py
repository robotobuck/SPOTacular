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