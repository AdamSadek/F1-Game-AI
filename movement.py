import pygame
import time
import random

class Movement:
    def move(surface, driver, track_layout, startingPos):
        turnNum = 1
        
        while turnNum < len(track_layout):
            nextX, nextY = track_layout[turnNum]
            distX = nextX - startingPos[0]
            distY = nextY - startingPos[1]
            if distX > 0:
                directionX = 1
            elif distX < 0:
                directionX = -1
            else:
                directionX = -1

            if distY > 0:
                directionY = 1
            elif distY < 0:
                directionY = -1
            else:
                directionY = 0

            startingPos[0] += directionX
            startingPos[1] += directionY

            # some colors :)
            WHITE = (255, 255, 255)
            BLACK = (0, 0, 0)
           
            # this will clear the surface before it draws, this way there won't be the red line bug.    
            surface.fill(WHITE)
            # drawing track
            pygame.draw.lines(surface, BLACK, True, track_layout, 15)  
            # drawing driver
            pygame.draw.circle(surface, driver.color, (int(startingPos[0]), int(startingPos[1])), 5)
            # updates the full display surface to the screen
            pygame.display.flip()
            # move to next turn on the track
            if startingPos[0] == nextX and startingPos[1] == nextY:
                turnNum += 1 
