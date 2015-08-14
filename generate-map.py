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
    draw_map(map)


def handle_events():
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        raise EndGameException()

if __name__ == '__main__':
    main()