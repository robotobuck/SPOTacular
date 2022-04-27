import randomRobotData
import auction

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