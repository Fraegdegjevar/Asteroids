import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", center = self.position, radius = self.radius, width = 2)
    
    def split(self):
        self.kill() #remove current object
        if self.radius <= ASTEROID_MIN_RADIUS:
            return #if this was small asteroid - no splitting required - we're done!
       
        random_angle = random.uniform(20,50)
        first_asteroid_velocity = self.velocity.rotate(random_angle)
        second_asteroid_velocity = self.velocity.rotate(-random_angle)
        asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
        
        first_asteroid = Asteroid(x = self.position.x, y = self.position.y, radius = asteroid_radius)
        first_asteroid.velocity = first_asteroid_velocity * 1.2

        second_asteroid = Asteroid(x = self.position.x, y = self.position.y, radius = asteroid_radius)
        second_asteroid.velocity = second_asteroid_velocity
        
    def update(self, dt):
        self.position += self.velocity * dt
