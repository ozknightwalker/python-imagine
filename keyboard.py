import pygame
from pygame import *


def get_direction_to_move():
    pressed_keys = pygame.key.get_pressed()
    x_dir = 0
    y_dir = 0
    if pressed_keys[K_LEFT]:
        x_dir -= 1
    if pressed_keys[K_RIGHT]:
        x_dir += 1
    if pressed_keys[K_DOWN]:
        y_dir += 1
    if pressed_keys[K_UP]:
        y_dir -= 1
    return x_dir, y_dir
