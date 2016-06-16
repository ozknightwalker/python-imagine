import pygame
import random
width, height = 700, 500
white = 255, 255, 255
black = 0, 0, 0


class Muppet(pygame.sprite.Sprite):

    def __init__(self, speed_x, speed_y, screen_width, screen_height, image):
        super(Muppet, self).__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
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
