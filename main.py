from area import AreaToSuvey
import randomRobotData
import auction
from relationship import RelationshipBetweenRobotAndArea
from robot import Robot

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

# Define area types
areas = []
areas.append(AreaToSuvey(10, 10, 'water'))
areas.append(AreaToSuvey(10, 10, 'grassy'))

# Define Robot Types
robots = []
robots.append(Robot('submarine'))

# Define Relationships
for a in areas:
  for r in robots:
    relationship = RelationshipBetweenRobotAndArea(r, a)
    relationship.displayRelationshipInfo()