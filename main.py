import sys

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot


def main():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    delta = 0
    running = True

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for item in updatable:
            item.update(delta)

        screen.fill("black")

        for item in asteroids:
            if item.check_collision(player):
                print("Game Over")
                running = False
                sys.exit()

        for asteroid in asteroids:
            for bullet in shots:
                if bullet.check_collision(asteroid):
                    asteroid.kill()

        for item in drawable:
            item.draw(screen)

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60 and saves delta in seconds
        delta = clock.tick(60) / 1000

    pygame.quit()

if __name__ == "__main__":
    main()