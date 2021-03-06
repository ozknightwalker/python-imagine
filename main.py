import sys
import pygame
from time import sleep
from pygame import *
from datetime import datetime

from stats import *
from keyboard import get_direction_to_move
from sprites import PlayerBlock, Muppet
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

muppet_group = pygame.sprite.Group()

for i in xrange(1, 15):
    muppet = Muppet(speed_x=random.randint(1, 3), speed_y=random.randint(1, 3), screen_width=width, screen_height=height, width=30, height=30, image="spritesheet.png", coordinates=sprite_coordinates[len(muppet_group)+1], id=i)
    muppet_group.add(muppet)

player = PlayerBlock(
    speed=5, screen_width=width, screen_height=height, image="spritesheet.png",
    width=30, height=30, coordinates=sprite_coordinates[0])
player.rect.x = width / 2
player.rect.y = height / 2

player_group = pygame.sprite.Group()
player_group.add(player)
start_time = datetime.now()

to_hit = 1
mup_to_hit_group = pygame.sprite.Group()
mup_to_hit = Muppet(speed_x=0, speed_y=0, screen_width=width, screen_height=height, width=25, height=25, image="spritesheet.png", coordinates=sprite_coordinates[to_hit], id=100)
mup_to_hit.rect.x = 40
mup_to_hit.rect.y = 5
mup_to_hit_group.add(mup_to_hit)

excludes = []

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

    mup_to_hit_group.draw(screen)

    muppet_group.draw(screen)
    muppet_group.update()
    player_group.draw(screen)
    player.update_movement(*get_direction_to_move())
    player_group.update()
    render_life(screen, life)
    # render_score(screen, score)
    time = datetime.now() - start_time
    t = int(time.total_seconds())
    render_time(screen, t)
    show_to_hit(screen, mup_to_hit_group)
    # Show Endgame
    # show_endgame(screen, t)
    pygame.display.flip()

    hit_muppets = pygame.sprite.spritecollide(player, muppet_group, True)
    for mup in hit_muppets:
        if mup.id != to_hit:
            life -= 1
            excludes.append(mup.id)
        else:
            to_hit += 1
            while to_hit in excludes:
                to_hit += 1

            if to_hit < 15:
                mup_to_hit = Muppet(speed_x=0, speed_y=0, screen_width=width, screen_height=height, width=25, height=25, image="spritesheet.png", coordinates=sprite_coordinates[to_hit], id=100)
                mup_to_hit.rect.x = 40
                mup_to_hit.rect.y = 5
                mup_to_hit_group.empty()
                mup_to_hit_group.add(mup_to_hit)

    if life == 0:
        game_over(screen)
        pygame.display.flip()
        sleep(5)
        break

    if len(muppet_group) == 0:
        # Show Endgame
        show_endgame(screen, t)
        pygame.display.flip()
        sleep(5)
        break
