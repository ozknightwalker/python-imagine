import sys
import pygame
from time import sleep
from pygame import *

from keyboard import get_direction_to_move
pygame.init()

size = width, height = 700, 500
speed = [2, 2]
white = 250, 250, 250

screen = pygame.display.set_mode(size)

ball = pygame.image.load("sample.png")
ballrect = ball.get_rect()

pygame.key.set_repeat(500, 30)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    sleep(0.0166)
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(white)
    screen.blit(ball, ballrect)
    pygame.display.flip()

    print get_direction_to_move()
