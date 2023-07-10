class Driver:
    def __init__(self, color, position, speed):
        self.color = color
        self.position = position
        self.speed = speed



    # def draw(self, surface):
    #     pygame.draw.circle(surface, self.color, (int(self.position[0]), int(self.position[1])), 5)
    # def update(self, surface):
    #     print(self.position[0])
    #     self.position[0] += self.speed
    #     self.position[1] += self.speed
    #     pygame.draw.circle(surface, self.color, (int(self.position[0]), int(self.position[1])), 5)