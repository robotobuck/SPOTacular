from area import AreaToSurvey
from auction import Auction
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
searchArea = [ [AreaToSurvey(30, 60, 'wooded', 0, 0), AreaToSurvey(30, 60, 'rocky', 0, 1), AreaToSurvey(30, 45, 'grassy', 0, 2), AreaToSurvey(30, 30, 'grassy', 0, 3)],
            [AreaToSurvey(45, 60, 'wooded', 1, 0), AreaToSurvey(45, 60, 'rocky', 1, 1), AreaToSurvey(45, 45, 'grassy', 1, 2), AreaToSurvey(45, 30, 'grassy', 1, 3)],
            [AreaToSurvey(60, 60, 'wooded', 2, 0), AreaToSurvey(60, 60, 'rocky', 2, 1), AreaToSurvey(60, 45, 'grassy', 2, 2), AreaToSurvey(60, 30, 'grassy', 2, 3)],
            [AreaToSurvey(60, 60, 'wooded', 3, 0), AreaToSurvey(60, 60, 'rocky', 3, 1), AreaToSurvey(60, 45, 'water', 3, 2), AreaToSurvey(60, 30, 'water', 3, 3)] ]

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
print()
auction.sequentialSingle(3, 1, Auction.DFS, False, False)
print()
auction.sequentialSingle(3, 1, Auction.BFS, True, False)
print()
auction.sequentialSingle(3, 1, Auction.DFS, True, False)
print()
auction.sequentialSingle(3, 1, Auction.BFS, True, True)
print()
auction.sequentialSingle(3, 1, Auction.DFS, True, True)
print()
auction.combinatorial(robots, searchArea)

# Define Relationships
#for r in range(len(searchArea)):
#    row = searchArea[r]
#    for c in range(len(row)):
#        for robot in robots:
#            print(robot.bidSimple(searchArea, r, c))
#            relationship = RelationshipBetweenRobotAndArea(robot, searchArea[r][c])
#            relationship.displayRelationshipInfo()