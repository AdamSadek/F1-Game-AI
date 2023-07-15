# Need to remove some disables when code is more refined.
# pylint: disable=chained-comparison,too-many-statements,too-many-branches,too-many-nested-blocks,missing-module-docstring,missing-class-docstring,invalid-name,too-many-locals,no-member,too-few-public-methods,no-self-argument,missing-function-docstring,import-error,line-too-long
import pygame

class Movement:
    def move(surface, drivers, track_layout, startingPos):
        # some colors :)
        # WHITE = (255, 255, 255)
        # BLACK = (0, 0, 0)
        turnNum = 1
        maxDiff = 9
        totalLapsDone = 0
        # create a separate position for each driver
        driverPositions = [startingPos.copy() for _ in drivers]
        while totalLapsDone != 3:
            lapsDone = set()
            for i, driver in enumerate(drivers):
                # check if all drivers have finished a lap
                if len(lapsDone) == len(drivers):
                    totalLapsDone += 1
                if driver.turnNum == len(track_layout):
                    driver.lapsDone += 1
                    driver.turnNum = 1
                    turnNum += 1
                    lapsDone.add(i)
                print("driver turn num = ", driver.turnNum)
                nextX, nextY = track_layout[driver.turnNum]
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

                print("next x = ", int(nextX))
                print("next y = ", int(nextY))
                posX, posY = map(int, driverPositions[i])

                diffX = abs(posX - nextX)
                diffY = abs(posY - nextY)

                print("diff x = ", diffX)
                print("diff y = ", diffY)

                # print("difference x = ", diffX, "\n", "difference x minus current pos = ", posX - diffX)
                if (diffX <= maxDiff) and (diffY <= maxDiff):
                    driver.turnNum += 1

                # if posX == nextX and posY == nextY:
                #     driver.turnNum += 1
                # else:
                #     print("driver speed =", driverSpeedX, " ", driverSpeedY)
                #     if posX != nextX:
                #         print("minus speed x = ", abs(driverSpeedX - posX))
                #         if (prevX > nextX and posX <= nextX) or (prevX < nextX and posX >= nextX):
                #             if (prevY - nextY > 0 and posY <= nextY) or (prevY - nextY < 0 and posY >= nextY):
                #                 driver.turnNum += 1
                #     else:
                #         if (prevY - nextY > 0 and posY <= nextY) or (prevY - nextY < 0 and posY >= nextY):
                #             driver.turnNum += 1


                # move to next turn on the track
                # if all(int(driverPositions[i][0]) == nextX
                #    and int(driverPositions[i][1]) == nextY for i in range(len(drivers))):
                #     turnNum += 1
