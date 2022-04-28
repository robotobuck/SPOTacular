import utils


class AreaToSuvey:
  def __init__(self, name, length, width, enviornment):
    self.__name = name
    self.__length = length
    self.__width = width
    self.__environmentType = enviornment

    self.checkAndSetEnvironmentType()
  
  def displayAreaDetails(self):
    print(f'Area \'{self.__name}\' details:')
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
  
  def getName(self):
    return self.__name