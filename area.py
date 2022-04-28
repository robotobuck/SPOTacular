import utils


class AreaToSurvey:
  def __init__(self, length, width, environment):
    self.__length = length
    self.__width = width
    self.__environmentType = environment

    self.checkAndSetEnvironmentType()
  
  def displayAreaDetails(self):
    print("Area Details: ")
    print(f'Length: {self.__length}')
    print(f'Width: {self.__width}')
    print(f'Type: {self.__environmentType}')

  def checkAndSetEnvironmentType(self):
    enviornmentOptions = utils.getAreaTypeList()
    if self.__environmentType not in enviornmentOptions:
      print(f"\nWarning!: Environment Type {self.__environmentType} not in list, being set to \'unkown\'\n")
      self.__environmentType = "unkown"

  def getLength(self):
    return self.__length
  
  def getWidth(self):
    return self.__width
  
  def getSurfaceArea(self):
    return self.__length * self.__width
  
  def getEnvironmentType(self):
    return self.__environmentType
  