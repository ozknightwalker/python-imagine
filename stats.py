import pygame

pygame.init()
myfont = pygame.font.SysFont("monospace", 16)

black = 0, 0, 0


def update_score(score, counter=1):
    return score + counter


def update_life(life, counter=1):
    return life + counter


def render_score(screen, score):
    x = screen.get_size()[0]
    text = myfont.render('Score: {}'.format(score), 1, black)
    screen.blit(text, ((x / 3), 10))


def render_life(screen, life):
    string = 'Life: {}'.format(life)
    x = screen.get_size()[0]
    text = myfont.render(string, 1, black)
    screen.blit(text, ((x / 2), 10))
