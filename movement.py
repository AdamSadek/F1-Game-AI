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

                driverPositions[i][0] += directionX * driver.speed
                driverPositions[i][1] += directionY * driver.speed
                print("Y direction: ", directionY)
                print("driver: ", driver.color)
                print("driver x: ",int(driverPositions[i][0]))
                print("driver y: ",int(driverPositions[i][1]))
            
                # this will clear the surface before it draws, this way there won't be the red line bug.    
                surface.fill(WHITE)
                # drawing track
                pygame.draw.lines(surface, BLACK, True, track_layout, 15)  
                # drawing driver
                pygame.draw.circle(surface, driver.color, (int(driverPositions[i][0]), int(driverPositions[i][1])), 5)
                # updates the full display surface to the screen
                pygame.display.flip()
                
                if (int(driverPositions[i][0]) == nextX or int(driverPositions[i][0]) == nextX - 1) and (int(driverPositions[i][1]) == nextY or int(driverPositions[i][1]) == nextY - 1):
                    driver.turnNum += 1
                # move to next turn on the track
                if all(int(driverPositions[i][0]) == nextX
                   and int(driverPositions[i][1]) == nextY for i in range(len(drivers))):
                    turnNum += 1
