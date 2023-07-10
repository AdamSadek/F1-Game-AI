import pygame
import time
import random

class Movement:
    def move(surface, drivers, track_layout, startingPos):
        # some colors :)
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        turnNum = 1
        driverPositions = [startingPos.copy() for _ in drivers]  # Create a separate position for each driver

        while turnNum < len(track_layout):
            for i, driver in enumerate(drivers):
                nextX, nextY = track_layout[turnNum]
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

                # startingPos[0] += directionX
                # startingPos[1] += directionY
                # print("driver initial pos: ",driverPositions[i][0])
                # print("dir x: ", (directionX * driver.speed))
                # print("dir y: ", (directionY * driver.speed))
            
                driverPositions[i][0] += (directionX)
                driverPositions[i][1] += (directionY)
                print("Y direction: ", directionY)
                print("driver: ", driver.color)
                print("driver x: ",driverPositions[i][0])
                print("driver y: ",driverPositions[i][1])
            
                # this will clear the surface before it draws, this way there won't be the red line bug.    
                surface.fill(WHITE)
                # drawing track
                pygame.draw.lines(surface, BLACK, True, track_layout, 15)  
                # drawing driver
                pygame.draw.circle(surface, driver.color, (int(driverPositions[i][0]), int(driverPositions[i][1])), 5)
                # updates the full display surface to the screen
                pygame.display.flip()
                # move to next turn on the track
                # if startingPos[0] == nextX and startingPos[1] == nextY:
                #     turnNum += 1 
                if all(driverPositions[i][0] == nextX and driverPositions[i][1] == nextY for i in range(len(drivers))):
                    turnNum += 1
