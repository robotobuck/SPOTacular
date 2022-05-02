from area import AreaToSurvey
import randomRobotData
from auction import Auction
from relationship import RelationshipBetweenRobotAndArea
from robot import Spot, AgileX, BlueROV2, IntelAero

# Constants
#NUM_OF_ROBOTS = 5
#NUM_OF_AREAS = 3
## This will be replaced when real data becomes available
## This should be called again for every new section of land to survey
#robotData = []
#for _ in range(NUM_OF_AREAS):
#    robotData.append(randomRobotData.generateRandomData(NUM_OF_ROBOTS))
#
#print("Robot stats by area: ")
#for areaStats in robotData:
#    print(areaStats)
#
## Find best robot for each area
#optimalRobots = auction.assignAreas(robotData)
#print("Optimal Robots: ", optimalRobots)


# Define search area
searchArea = [ [AreaToSurvey(10, 20, 'wooded', 0, 0), AreaToSurvey(10, 20, 'rocky', 0, 1), AreaToSurvey(10, 15, 'grassy', 0, 2), AreaToSurvey(10, 10, 'grassy', 0, 3)],
            [AreaToSurvey(15, 20, 'wooded', 1, 0), AreaToSurvey(15, 20, 'rocky', 1, 1), AreaToSurvey(15, 15, 'grassy', 1, 2), AreaToSurvey(15, 10, 'grassy', 1, 3)],
            [AreaToSurvey(20, 20, 'wooded', 2, 0), AreaToSurvey(20, 20, 'rocky', 2, 1), AreaToSurvey(20, 15, 'grassy', 2, 2), AreaToSurvey(20, 10, 'grassy', 2, 3)],
            [AreaToSurvey(20, 20, 'wooded', 3, 0), AreaToSurvey(20, 20, 'rocky', 3, 1), AreaToSurvey(20, 15, 'water', 3, 2), AreaToSurvey(20, 10, 'water', 3, 3)] ]

for r in range(len(searchArea)):
    for c in range(len(searchArea[0])):
        if r>0:
            y = searchArea[r-1][c].center['y'] + searchArea[r-1][c].getHeight()/2 + searchArea[r][c].getHeight()/2
        else:            
            y = searchArea[0][c].getHeight()/2

        if c>0:
            x = searchArea[r][c-1].center['x'] + searchArea[r][c-1].getWidth()/2 + searchArea[r][c].getWidth()/2
        else:            
            x = searchArea[r][0].getWidth()/2

        searchArea[r][c].center = { 'x':x, 'y':y }

# Initialize Robots
startRow = 3
startCol = 1
startArea = searchArea[startRow][startCol]
startArea2 = searchArea[startRow][startCol+1]
robots = [ Spot(startArea.center), AgileX(startArea.center), BlueROV2(startArea2.center), IntelAero(startArea.center) ]

#run auctions
auction = Auction(robots, searchArea)
auction.sequentialSingle(3, 1, Auction.BFS, False, False)
auction.sequentialSingle(3, 1, Auction.DFS, False, False)
auction.sequentialSingle(3, 1, Auction.BFS, True, False)
auction.sequentialSingle(3, 1, Auction.DFS, True, False)
auction.combinatorial(robots, searchArea)

# Define Relationships
#for r in range(len(searchArea)):
#    row = searchArea[r]
#    for c in range(len(row)):
#        for robot in robots:
#            print(robot.bidSimple(searchArea, r, c))
#            relationship = RelationshipBetweenRobotAndArea(robot, searchArea[r][c])
#            relationship.displayRelationshipInfo()