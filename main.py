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



# Initialize Robots
robots = [ Spot(), AgileX(), BlueROV2(), IntelAero() ]

# Define search area
searchArea = [ [AreaToSurvey(10, 10, 'grassy'), AreaToSurvey(10, 10, 'wooded'), AreaToSurvey(20, 20, 'rocky'), AreaToSurvey(15, 15, 'grassy')],
            [AreaToSurvey(10, 10, 'wooded'), AreaToSurvey(10, 10, 'wooded'), AreaToSurvey(20, 20, 'water'), AreaToSurvey(15, 15, 'grassy')],
            [AreaToSurvey(10, 10, 'rocky'), AreaToSurvey(10, 10, 'wooded'), AreaToSurvey(20, 20, 'water'), AreaToSurvey(15, 15, 'grassy')] ]

# run auctions
auction = Auction()
print(auction.sequentialSingle(searchArea, Auction.BFS))
print(auction.sequentialSingle(searchArea, Auction.DFS))

# Define Relationships
#for r in range(len(searchArea)):
#    row = searchArea[r]
#    for c in range(len(row)):
#        for robot in robots:
#            print(robot.bidSimple(searchArea, r, c))
#            relationship = RelationshipBetweenRobotAndArea(robot, searchArea[r][c])
#            relationship.displayRelationshipInfo()