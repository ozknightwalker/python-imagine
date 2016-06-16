import pygame

from spritesheet import Spritesheet

class Block(pygame.sprite.Sprite):
    def __init__(self, image, width, height, coordinates):
        print image
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
        self.screen_width = screen_width
        self.screen_height = screen_height

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
