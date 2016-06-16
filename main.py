import sys
import pygame
from time import sleep
from pygame import *
from datetime import datetime

from stats import *
from keyboard import get_direction_to_move
from sprites import PlayerBlock
from muppet import Muppet
import random
pygame.init()

size = width, height = 700, 500
speed = [2, 2]
white = 250, 250, 250
score = 0
life = 5
time = 0

sprite_coordinates=[(10, 20, 95, 120), (100, 20, 95, 120), (200, 20, 95, 120),
                    (300, 20, 95, 130), (400, 20, 85, 130),
                    (480, 20, 100, 120), (590, 20, 80, 120),
                    (10, 150, 95, 110), (110, 150, 90, 110),
                    (200, 150, 90, 110), (300, 150, 90, 110),
                    (400, 150, 90, 110), (480, 150, 90, 115),
                    (580, 150, 90, 115), (10, 260, 95, 120)]

screen = pygame.display.set_mode(size)

ball = pygame.image.load("sample.png")
ballrect = ball.get_rect()

pygame.key.set_repeat(500, 30)

player = PlayerBlock(
    speed=5, screen_width=width, screen_height=height, image="sample.png",
    width=30, height=30)
player.rect.x = width / 2
player.rect.y = height / 2

player_group = pygame.sprite.Group()
player_group.add(player)
muppet_group = pygame.sprite.Group()
start_time = datetime.now()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    sleep(0.0166)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
    screen.fill(white)

    player_group.draw(screen)
    player.update_movement(*get_direction_to_move())
    player_group.update()
    muppet_group.draw(screen)
    for muppet in muppet_group:
        muppet.update()
    while len(muppet_group) < 5:
        muppet = Muppet(speed_x=random.randint(0, 9), speed_y=random.randint(0, 9), screen_width=width, screen_height=height, image="ball.gif")
        muppet_group.add(muppet)
        muppet_group.update()
    render_life(screen, life)
    render_score(screen, score)
    time = datetime.now() - start_time
    t = int(time.total_seconds())
    render_time(screen, t)
    pygame.display.flip()
