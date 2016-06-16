import pygame

pygame.init()
pygame.display.set_caption("testing")

myfont = pygame.font.SysFont("monospace", 16)
black = 0, 0, 0


def update_score(score, counter=1):
    return score + counter


def update_life(life, counter=1):
    return life + counter

# def draw_stats(score, life):
#   black = 0, 0, 0
#   scoretext = myfont.render("Score: {0}".format(score), 1, black)
#     lifetext = myfont.render("Lives: {0}".format(life), 1, black)


def render_score(screen, score):
    x = screen.get_size()[0]
    text = myfont.render('Score: {}'.format(score), 1, black)
    screen.blit(text, ((x / 3), 10))


def render_life(screen, life):
    string = 'Life: {}'.format(life)
    x, y = screen.get_size()
    text = myfont.render(string, 1, black)
    screen.blit(text, ((x / 2), 10))
