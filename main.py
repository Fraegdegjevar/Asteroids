import pygame
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    GameClock = pygame.time.Clock()
    dt = 0
    
    #Creating groups for updatable and drawable objects
    # These can be added as containers to each class and will ensure
    #all instances are in the group
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # type: ignore

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill(color = (1,1,1))
        
        updatable.update(dt)
        
        for object in drawable:
            object.draw(screen)
        
        pygame.display.flip()
        
        #limit frame rate to 60 fps and store delta time in dt
        dt = GameClock.tick(60) / 1000

if __name__ == "__main__":
    main()
