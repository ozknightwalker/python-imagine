import pygame
from pygame import *


def get_direction_to_move():
    pressed_keys = pygame.key.get_pressed()
    x_dir = 0
    y_dir = 0
    if pressed_keys[K_LEFT]:
        print 'left'
        x_dir -= 1
    if pressed_keys[K_RIGHT]:
        print 'right'
        x_dir += 1
    if pressed_keys[K_DOWN]:
        print 'down'
        y_dir += 1
    if pressed_keys[K_UP]:
        print 'up'
        y_dir -= 1
    return x_dir, y_dir
