import pygame
import random

from spritesheet import Spritesheet


class Block(pygame.sprite.Sprite):
    def __init__(self, image, width, height, coordinates):
        pygame.sprite.Sprite.__init__(self)
        sheet = Spritesheet(image)
        self.image = sheet.get_image(coordinates)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()


class PlayerBlock(Block):
    def __init__(self, speed, screen_width, screen_height,
                 *args, **kwargs):
        super(PlayerBlock, self).__init__(*args, **kwargs)
        self.base_speed = speed
        self.x_speed = 0
        self.y_speed = 0
        self.screen_width = screen_width - kwargs['width']
        self.screen_height = screen_height - kwargs['height']

    def update_movement(self, x_dir, y_dir):
        self.x_speed = x_dir * self.base_speed
        self.y_speed = y_dir * self.base_speed

    def update(self):
        new_x = self.rect.x + self.x_speed
        new_y = self.rect.y + self.y_speed
        if new_y <= self.screen_height and new_y > 0:
            self.rect.y = new_y
        if new_x <= self.screen_width and new_x > 0:
            self.rect.x = new_x


class Muppet(Block):

    def __init__(self, id, speed_x, speed_y, screen_width, screen_height, *args, **kwargs):
        super(Muppet, self).__init__(*args, **kwargs)
        self.id = id
        self.x_speed = speed_x
        self.y_speed = speed_y
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.direction_y = 1
        self.direction_x = 1
        self.rect.x = random.randrange(screen_width - self.rect.size[0])
        self.rect.y = random.randrange(screen_height - self.rect.size[1])

    def update(self):
        new_x = self.rect.x + (self.x_speed * self.direction_x)
        new_y = self.rect.y + (self.y_speed * self.direction_y)

        if new_y <= (self.screen_height - self.rect.size[1]) and new_y > 0:
            self.rect.y = new_y
        else:
            self.direction_y *= -1
        if new_x <= (self.screen_width - self.rect.size[0]) and new_x > 0:
            self.rect.x = new_x
        else:
            self.direction_x *= -1
