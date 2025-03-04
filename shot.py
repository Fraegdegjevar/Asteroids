import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    #note that velocity is inherited from CircleShape
    def __init__(self, x, y):
        super().__init__(x = x, y = y, radius = SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", center = self.position, radius = self.radius, width = 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
