import pygame
class Driver:
    def __init__(self, color, position, speed):
        self.color = color
        self.position = position
        self.speed = speed

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.position[0]), int(self.position[1])), 5)