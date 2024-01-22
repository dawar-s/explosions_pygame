import random

import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from particles import Particle, ExplodingParticle
from random import choice, randint, uniform
from glob import glob

surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

particle_group = pygame.sprite.Group()

floating_particle_timer = pygame.event.custom_type()
pygame.time.set_timer(floating_particle_timer, 10)
sounds_files = [file for file in glob('./audio/*.wav')]


def spawn_particles(n: int):
    pygame.mixer.Sound(random.choice(sounds_files)).play()
    for _ in range(n):
        pos = pygame.mouse.get_pos()
        color = choice(('red', 'green', 'blue'))
        direction = pygame.math.Vector2(uniform(-1, 1), uniform(-1, 1)).normalize()
        speed = randint(50, 400)
        Particle(groups=particle_group, pos=pos, color=color, direction=direction, speed=speed)


def spawn_exploding_particles(n: int):
    pygame.mixer.Sound(random.choice(sounds_files)).play()
    for _ in range(n):
        pos = pygame.mouse.get_pos()
        color = choice(('lime', 'magenta', 'purple'))
        direction = pygame.math.Vector2(uniform(-0.2, 0.2), uniform(-1, 0)).normalize()
        speed = randint(50, 400)
        ExplodingParticle(groups=particle_group, pos=pos, color=color, direction=direction, speed=speed)


def spawn_floating_particles():
    init_pos = pygame.mouse.get_pos()
    pos = init_pos[0] + randint(-10, 10), init_pos[1] + randint(-10, 10)
    color = 'gold'
    direction = pygame.math.Vector2(0, -1).normalize()
    speed = randint(50, 100)
    Particle(groups=particle_group, pos=pos, color=color, direction=direction, speed=speed)


def main_loop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    spawn_particles(1000)
                elif pygame.mouse.get_pressed()[2]:
                    spawn_exploding_particles(1000)
            if event.type == floating_particle_timer:
                spawn_floating_particles()

        dt = clock.tick() / 1000

        surface.fill('black')
        particle_group.draw(surface)

        particle_group.update(dt)
        pygame.display.update()


if __name__ == '__main__':
    pygame.init()
    main_loop()
