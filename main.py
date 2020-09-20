import os.path
import random
import pygame
from pygame.locals import *

pygame.init()
pygame.font.init()

move = [False, False, False, False]
rotate = [100]

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("PYRKAN")

move_step = 4

box = pygame.Rect((0,0),(400,200))
surface = pygame.Surface((590,350))
bottom_surface = pygame.Surface((600, 50))
player_up_event = pygame.event.Event(pygame.USEREVENT,{'code': 'player.up'})

#star = pygame.image.load(os.path.join('assets','star.png'))
canvas = pygame.image.load(os.path.join('assets','canvas.png'))

font = pygame.font.Font(None, 12)
text = font.render('PLAYER UP', 1, (100,255,100))
textpos = text.get_rect()
textpos.centerx = surface.get_rect().centerx

def make_bricks(rows = 5):
    bricks = []
    for row in range(rows):
        for col in range(23):
            brick = pygame.Surface((21,9))
            brick.fill(pygame.Color(random.randrange(255),random.randrange(255),random.randrange(255)))
            bricks.append((brick, ((4 * col) + col * 21, 13 + row * 9)))
    return bricks

def draw_sky(star):
    for row in range(11):
        for col in range(19):
            star_animation(star, (col * star.get_rect().width, row * star.get_rect().height))

def make_a_star(size):
    star = pygame.Surface((size, size))
    star.fill(pygame.Color(255,255,255))
    back_color = pygame.Color(0,0,0)
    pygame.draw.circle(star, back_color,(0,0),int(size/2),0)
    pygame.draw.circle(star, back_color,(0, size),int(size/2),0)
    pygame.draw.circle(star, back_color,(size,0),int(size/2),0)
    pygame.draw.circle(star, back_color,(size, size),int(size/2),0)
    star.set_colorkey(back_color)
    return star

def press_key(key):
    if key == K_LEFT:
        move[0] = True
    if key == K_RIGHT:
        move[1] = True
    if key == K_UP:
        move[2] = True
    if key == K_DOWN:
        move[3] = True
    if key == K_ESCAPE:
        quit()
def release_key(key):
    if key == K_LEFT:
        move[0] = False
    if key == K_RIGHT:
        move[1] = False
    if key == K_UP:
        move[2] = False
    if key == K_DOWN:
        move[3] = False

def process_user_event(code):
    if code == 'player.up': player_up()

def star_animation(star, place):
    img = pygame.transform.scale(star, (16,16))
    img = pygame.transform.rotate(img, rotate[0])
    x_dist = (img.get_rect().width - 16)/2
    y_dist = (img.get_rect().height - 16)/2
    surface.blit(img, (place[0] - x_dist, place[1] - y_dist))

def work():
    #print(textpos.centerx - surface.get_rect().centerx)
    if textpos.centerx - surface.get_rect().centerx < -80 : move[0] = False
    if textpos.centerx - surface.get_rect().centerx > 80 : move[1] = False
    if move[0]: textpos.centerx -= move_step
    if move[1]: textpos.centerx += move_step
    if move[2]: textpos.y -= move_step
    if move[3]: textpos.y += move_step
    rotate[0] += 15
    if rotate[0] > 360: rotate[0] = 0

def display():
    surface.fill(pygame.Color(0,0,0))
    draw_sky(Star)
    for brick in Bricks:
        surface.blit(brick[0], brick[1])
    screen.blit(surface,(5,0))
    bottom_surface.fill(pygame.Color(180,180,180))
    screen.blit(bottom_surface, (0, 350))

Bricks = make_bricks()
Star = make_a_star(32)
pygame.time.set_timer(USEREVENT + 1, 18)
event = pygame.event.wait()
while event:
    if event.type == QUIT: quit()
    elif event.type == KEYDOWN: press_key(event.key)
    elif event.type == KEYUP: release_key(event.key)
    elif event.type == USEREVENT: process_user_event(event.code)
    elif event.type == USEREVENT + 1: 
        work()
        display()
        pygame.display.flip()
    event = pygame.event.wait()