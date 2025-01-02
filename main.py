import pygame
from constants import *
from player import Player


def main():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    delta = 0
    running = True

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player.update(delta)
        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")

        # RENDER YOUR GAME HERE
        player.draw(screen)

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60 and saves delta in seconds
        delta = clock.tick(60) / 1000

    pygame.quit()

if __name__ == "__main__":
    main()