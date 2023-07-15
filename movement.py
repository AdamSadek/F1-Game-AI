# Need to remove some disables when code is more refined.
# pylint: disable=chained-comparison,too-many-statements,too-many-branches,too-many-nested-blocks,missing-module-docstring,missing-class-docstring,invalid-name,too-many-locals,no-member,too-few-public-methods,no-self-argument,missing-function-docstring,import-error,line-too-long
import pygame

class Movement:
    def move(surface, drivers, track_layout, startingPos):
        turnNum = 1
        maxDiff = 9
        totalLapsDone = 0
        # create a separate position for each driver
        driverPositions = [startingPos.copy() for _ in drivers]
        while totalLapsDone != 3:
            lapsDone = set()
            for i, driver in enumerate(drivers):
                # checks if all drivers have finished a lap
                if len(lapsDone) == len(drivers):
                    totalLapsDone += 1

                # checks if a driver completed a lap
                if driver.turnNum == len(track_layout):
                    driver.lapsDone += 1
                    driver.turnNum = 1
                    turnNum += 1
                    lapsDone.add(i)

                # getting the next turn coordinates
                nextX, nextY = track_layout[driver.turnNum]

                # getting the distance between the drivers position and the next position
                distX = nextX - driverPositions[i][0]
                distY = nextY - driverPositions[i][1]

                # checking which direction to go to based on the distance
                if distX > 0:
                    directionX = 1
                elif distX < 0:
                    directionX = -1
                else:
                    directionX = 0

                if distY > 0:
                    directionY = 1
                elif distY < 0:
                    directionY = -1
                else:
                    directionY = 0

                # Adding speed to the direction and then adding it to the drivers position
                driverSpeedX = directionX * driver.speed
                driverSpeedY = directionY * driver.speed

                driverPositions[i][0] += driverSpeedX
                driverPositions[i][1] += driverSpeedY

                # drawing driver
                pygame.draw.circle(surface, driver.color, (int(driverPositions[i][0]), int(driverPositions[i][1])), 7)

                # updates the full display surface to the screen
                pygame.display.flip()

                # getting current position (might not need this really) 
                posX, posY = map(int, driverPositions[i])

                # getting the difference between the drivers position and the next position.
                diffX = abs(posX - nextX)
                diffY = abs(posY - nextY)

                # checks if the driver reached the corner (needs improving as it's not an ideal check. Might show problems later on)
                if (diffX <= maxDiff) and (diffY <= maxDiff):
                    driver.turnNum += 1