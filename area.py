import utils


class AreaToSuvey:
  def __init__(self, name, length, width, enviornment):
    self.name = name
    self.length = length
    self.width = width
    self.environmentType = enviornment

    self.checkAndSetEnvironmentType()
  
  def displayAreaDetails(self):
    print(f'Area \'{self.name}\' details:')
    print(f'Length: {self.length}')
    print(f'Width: {self.width}')
    print(f'Type: {self.environmentType}')

  def checkAndSetEnvironmentType(self):
    enviornmentOptions = utils.getAreaTypeList()
    if self.environmentType not in enviornmentOptions:
      print(f"\nWarning!: Environment Type {self.environmentType} not in list, being set to \'unkown\'\n")
      self.environmentType = "unkown"