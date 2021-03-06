import pygame

pygame.init()
myfont = pygame.font.SysFont("monospace", 16)

black = 0, 0, 0
white = 255, 255, 255


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


def render_time(screen, time):
    string = 'Time: {}'.format(time)
    x = screen.get_size()[0]
    text = myfont.render(string, 1, black)
    screen.blit(text, ((x / 1.5), 10))


def show_endgame(screen, time):
    screen.fill(white)
    myfont = pygame.font.SysFont("monospace", 25)
    x, y = screen.get_size()
    text = myfont.render("Congrats You finished the game in", 1, black)
    screen.blit(text, ((x / 12), (y / 2)))
    text = myfont.render("{} second/s".format(time), 1, black)
    screen.blit(text, ((x / 2.5), (y / 1.5)))


def show_to_hit(screen, group):
    x = screen.get_size()[0]
    text = myfont.render('Hit: ', 1, black)
    screen.blit(text, (0, 10))
    group.draw(screen)


def game_over(screen):
    screen.fill(white)
    myfont = pygame.font.SysFont("monospace", 25)
    x, y = screen.get_size()
    text = myfont.render("Game Over", 1, black)
    screen.blit(text, ((x / 2.5), (y / 2)))
    text = myfont.render("\"The best way to find happiness", 1, black)
    screen.blit(text, ((x / 6), (y / 1.5)))
    text = myfont.render("is to stop looking so hard\"", 1, black)
    screen.blit(text, ((x / 3), (y / 1.3)))
