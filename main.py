from area import AreaToSurvey
import randomRobotData
import auction
from relationship import RelationshipBetweenRobotAndArea
from robot import Spot, AgileX, BlueROV2, IntelAero

# Constants
NUM_OF_ROBOTS = 5
NUM_OF_AREAS = 3
# This will be replaced when real data becomes available
# This should be called again for every new section of land to survey
robotData = []
for _ in range(NUM_OF_AREAS):
    robotData.append(randomRobotData.generateRandomData(NUM_OF_ROBOTS))

print("Robot stats by area: ")
for areaStats in robotData:
    print(areaStats)

# Find best robot for each area
optimalRobots = auction.assignAreas(robotData)
print("Optimal Robots: ", optimalRobots)

# Define area
areas = [ [AreaToSurvey(10, 10, 'grassy'), AreaToSurvey(10, 10, 'wooded'), AreaToSurvey(20, 20, 'rocky'), AreaToSurvey(15, 15, 'grassy')],
            [AreaToSurvey(10, 10, 'wooded'), AreaToSurvey(10, 10, 'wooded'), AreaToSurvey(20, 20, 'water'), AreaToSurvey(15, 15, 'grassy')],
            [AreaToSurvey(10, 10, 'rocky'), AreaToSurvey(10, 10, 'wooded'), AreaToSurvey(20, 20, 'water'), AreaToSurvey(15, 15, 'grassy')] ]


# Define Robot Types
robots = []
robots.append(Spot())
robots.append(AgileX())
robots.append(BlueROV2())
robots.append(IntelAero())


# Define Relationships
for areaRow in areas:
    for a in areaRow:
        for r in robots:
            relationship = RelationshipBetweenRobotAndArea(r, a)
            relationship.displayRelationshipInfo()
