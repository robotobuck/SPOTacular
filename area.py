class AreaToSurvey:
    def __init__(self, height, width, environment, row, col):
        self.__height = height
        self.__width = width
        self.__environmentType = environment

        #to help with searches
        self.visited = False
        self.processed = False
        self.row = row
        self.col = col
        self.center = { 'x':0, 'y':0 }

        if row == 0:
            self.r = 'A'
        elif row == 1:
            self.r = 'B'
        elif row == 2:
            self.r = 'C'
        elif row == 3:
            self.r = 'D'
        else:
            self.r = 'Invalid'

        self.c = col

    def __reset(self):
        self.visited = False
        self.processed = False
  
    def displayAreaDetails(self):
        print("Area Details: ")
        print(f'Length: {self.__length}')
        print(f'Width: {self.__width}')
        print(f'Type: {self.__environmentType}') 

    def getHeight(self):
        return self.__height
  
    def getWidth(self):
        return self.__width
  
    def getSurfaceArea(self):
        return self.__height * self.__width
  
    def getEnvironmentType(self):
        return self.__environmentType
  