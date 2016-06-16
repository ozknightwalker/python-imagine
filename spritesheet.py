import pygame


class Spritesheet(object):
    def __init__(self, filename):
        self.sheet = pygame.image.load(filename).convert()

    def get_image(self, rectangle):
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        return image
