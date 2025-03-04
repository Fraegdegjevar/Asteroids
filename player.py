from circleshape import CircleShape
from constants import *
from shot import Shot
import pygame

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x = x, y = y, radius = PLAYER_RADIUS) # type: ignore
        self.rotation = 0
        self.shoot_timer = 0
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white",  self.triangle(), 2)
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def move(self, dt):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        
    def shoot(self):
        """shot velocity vector determined by rotating a y basis vector to match the player's
        rotation (direction) and given magnitude of 1*PLAYER_SHOOT_SPEED
        only shoots if shoot timer is 0. if we shoot, increase timer by shot cooldown constant.
        """
        if self.shoot_timer > 0:
            return
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN
        #use .x and .y to access the x and y coordinates of the player's position Vector2
        shot = Shot(x = self.position.x, y = self.position.y)
        shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
    
    def update(self, dt):
        #decrease shot timer by delta time from last frame
        self.shoot_timer -= dt
        
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()