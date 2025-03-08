import pygame
import sys
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # type: ignore
    GameClock = pygame.time.Clock()
    dt = 0
    
    #Creating groups for updatable and drawable objects
    # These can be added as containers to each class and will ensure
    #all instances are in the group
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Shot.containers = (updatable, drawable, shots)
    Player.containers = (updatable, drawable)
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        
        #check each object in the asteroids container group
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit(0)
            
            #after checking if the asteroid has killed the player, check if it
            # collides with any shots on screen and remove both if so.
            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()
        
        screen.fill(color = (1,1,1))
        
        for object in drawable:
            object.draw(screen)
        
        pygame.display.flip()
        
        #limit frame rate to 60 fps and store delta time in dt
        dt = GameClock.tick(60) / 1000

if __name__ == "__main__":
    main()
