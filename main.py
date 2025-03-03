from constants import *
import pygame

def main():
    pygame.init()
    GameClock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # type: ignore
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill(color = (1,1,1))
        pygame.display.flip()
        
        #limit frame rate to 60 fps and store delta time in dt
        dt = GameClock.tick(60) / 1000

if __name__ == "__main__":
    main()
