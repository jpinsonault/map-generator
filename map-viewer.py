__author__ = 'joe'
import os
import pygame
import sys
import random
import pickle
from random import randrange
from random import randint
from random import uniform
from pprint import pprint
from pygame import draw
from pygame.locals import *
from collections import deque
from collections import namedtuple
from pygame import gfxdraw
from generate_map import generate_heightmap


BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
BLUE = ( 0, 0, 255)
GREEN = ( 0, 255, 0)
RED = (255, 0, 0)
DARKGREEN = (0, 151, 0)

class EndGameException(Exception):
    pass


def main():
    screen = pygame.display.set_mode((640, 400))

    while True:
        try:
            game_loop(screen)
        except EndGameException:
            break


def game_loop(screen):
    handle_events()
    map_data = generate_heightmap(64, 16)
    draw_map(screen, map_data)


def handle_events():
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        raise EndGameException()


def draw_map(screen, map_data):
    screen.fill(BLACK)

    for y in range(256):
        for x in range(256):
            intensity = map_data[y][x]
            gfxdraw.pixel(screen, x, y, (intensity, intensity, intensity))

    pygame.display.flip()

if __name__ == '__main__':
    main()