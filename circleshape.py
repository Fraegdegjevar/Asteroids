import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
    
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
    
    def draw(self, screen):
        #sub-class/children must override this method
        pass
    
    def update(self, dt):
        #sub-class/children must override this method
        pass
    
    #If the euclidean distance between the positions (which are 2d vectors drawn from
    # origin to the centre point of the circleshapes) is <= the sum of the
    #circleshapes' radii, then these circles have collided. Returns True/False.
    def collides_with(self, other_collidable):
        distance = self.position.distance_to(other_collidable.position)
        
        return distance <= self.radius + other_collidable.radius