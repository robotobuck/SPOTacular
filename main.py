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
searchArea = [ [AreaToSurvey(10, 10, 'grassy', 0, 0), AreaToSurvey(10, 10, 'wooded', 0, 1), AreaToSurvey(20, 20, 'rocky', 0, 2), AreaToSurvey(15, 15, 'grassy', 0, 3)],
            [AreaToSurvey(10, 10, 'grassy', 1, 0), AreaToSurvey(10, 10, 'wooded', 1, 1), AreaToSurvey(20, 20, 'rocky', 1, 2), AreaToSurvey(15, 15, 'grassy', 1, 3)],
            [AreaToSurvey(10, 10, 'grassy', 2, 0), AreaToSurvey(10, 10, 'wooded', 2, 1), AreaToSurvey(20, 20, 'rocky', 2, 2), AreaToSurvey(15, 15, 'grassy', 2, 3)],
            [AreaToSurvey(10, 10, 'grassy', 3, 0), AreaToSurvey(10, 10, 'wooded', 3, 1), AreaToSurvey(20, 20, 'rocky', 3, 2), AreaToSurvey(15, 15, 'grassy', 3, 3)] ]


# Initialize Robots
startRow = 3
startCol = 1
robots = [ Spot(startRow, startCol), AgileX(startRow, startCol), BlueROV2(startRow, startCol), IntelAero(startRow, startCol) ]

#run auctions
auction = Auction(robots, searchArea)
auction.sequentialSingle(3, 1, Auction.BFS)
auction.sequentialSingle(3, 1, Auction.DFS)
auction.combinatorial(robots, searchArea)

# Define Relationships
#for r in range(len(searchArea)):
#    row = searchArea[r]
#    for c in range(len(row)):
#        for robot in robots:
#            print(robot.bidSimple(searchArea, r, c))
#            relationship = RelationshipBetweenRobotAndArea(robot, searchArea[r][c])
#            relationship.displayRelationshipInfo()