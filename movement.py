# Need to remove some disables when code is more refined.
# pylint: disable=too-many-statements,too-many-branches,too-many-nested-blocks,missing-module-docstring,missing-class-docstring,invalid-name,too-many-locals,no-member,too-few-public-methods,no-self-argument,missing-function-docstring,import-error,line-too-long
import pygame

class Movement:
    def move(surface, drivers, track_layout, startingPos):
        # some colors :)
        # WHITE = (255, 255, 255)
        # BLACK = (0, 0, 0)
        turnNum = 1
        # create a separate position for each driver
        driverPositions = [startingPos.copy() for _ in drivers]
        prevX, prevY = startingPos.copy()
        while turnNum < len(track_layout):
            for i, driver in enumerate(drivers):
                prevX, prevY = track_layout[driver.turnNum-1]
                nextX, nextY = track_layout[driver.turnNum]
                # distX = nextX - startingPos[0]
                # distY = nextY - startingPos[1]
                distX = nextX - driverPositions[i][0]
                distY = nextY - driverPositions[i][1]
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

                driverSpeedX = directionX * driver.speed
                driverSpeedY = directionY * driver.speed

                driverPositions[i][0] += driverSpeedX
                driverPositions[i][1] += driverSpeedY
                print("driver: ", driver.color)
                print("driver x: ",int(driverPositions[i][0]))
                print("driver y: ",int(driverPositions[i][1]))

                # drawing track
                # pygame.draw.lines(surface, BLACK, True, track_layout, 15)
                # drawing driver
                pygame.draw.circle(surface, driver.color, (int(driverPositions[i][0]), int(driverPositions[i][1])), 7)
                # updates the full display surface to the screen
                pygame.display.flip()

                print("driver speed = ", int(driverSpeedX))
                print("next = ", int(nextX))
                if int(driverPositions[i][0]) == nextX and int(driverPositions[i][1]) == nextY:
                    driver.turnNum += 1
                else:
                    print("prev x = ", prevX)
                    print("next x = ", nextX)
                    if int(driverPositions[i][0]) != nextX:
                        if prevX - nextX > 0:
                            if int(driverPositions[i][0]) <= nextX:
                                if prevY - nextY > 0:
                                    if int(driverPositions[i][1]) <= nextY:
                                        driver.turnNum += 1
                                elif prevY - nextY < 0:
                                    if int(driverPositions[i][1]) >= nextY:
                                        driver.turnNum += 1
                                else:
                                    driver.turnNum += 1
                        elif prevX - nextX < 0:
                            if int(driverPositions[i][0]) >= nextX:
                                if prevY - nextY > 0:
                                    if int(driverPositions[i][1]) <= nextY:
                                        driver.turnNum += 1
                                elif prevY - nextY < 0:
                                    if int(driverPositions[i][1]) >= nextY:
                                        driver.turnNum += 1
                                else:
                                    driver.turnNum += 1
                    else:
                        if prevY - nextY > 0:
                            if int(driverPositions[i][1]) <= nextY:
                                driver.turnNum += 1
                        elif prevY - nextY < 0:
                            if int(driverPositions[i][1]) >= nextY:
                                driver.turnNum += 1
                        else:
                            driver.turnNum += 1

                # move to next turn on the track
                # if all(int(driverPositions[i][0]) == nextX
                #    and int(driverPositions[i][1]) == nextY for i in range(len(drivers))):
                #     turnNum += 1
