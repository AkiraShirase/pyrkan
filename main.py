import os.path
import random
import pygame
import math
from pygame.locals import *

pygame.init()
pygame.font.init()

move = [False, False, False, False]
rotate = [100]

score = 0

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("PYRKAN")

move_step = 8

game_surface = pygame.Surface((590,380))
game_surface_rect = game_surface.get_rect()
game_surface_rect.top = 20
game_surface_rect.left = 5
score_surface = pygame.Surface((600, 20))
score_surface_rect = game_surface.get_rect()
score_surface_rect.top = 0
score_surface_rect.left = 0
player_surface = pygame.Surface((590, 20))
player_surface_rect = player_surface.get_rect()
player_surface_rect.top = 360
player_surface_rect.left = 5
player_up_event = pygame.event.Event(pygame.USEREVENT,{'code': 'player.up'})

font = pygame.font.Font(None, 12)

player = pygame.sprite.Sprite()
player.image = pygame.Surface((48, 12))
player.rect = pygame.Rect((player_surface_rect.width / 2) - 24, 0, 48, 12)
player.image.fill(pygame.Color(200,175,150))
player_group = pygame.sprite.Group()
player_group.add(player)

star_group = pygame.sprite.Group()

def rad(angle):
    return angle * (math.pi / 180)

def moveX(angle):
    return math.cos(rad(angle))
def moveY(angle):
    return math.sin(rad(angle))

def make_bricks(rows = 5):
    bricks = pygame.sprite.Group()
    for row in range(rows):
        for col in range(23):
            brick = pygame.sprite.Sprite()
            brick.image = pygame.Surface((21,9))
            brick.image.fill(pygame.Color(random.randrange(255),random.randrange(255),random.randrange(255)))
            brick.rect = pygame.Rect(((4 * col) + col * 21, 13 + row * 9), (21,9))
            bricks.add(brick)
    return bricks

def draw_sky(star):
    for row in range(11):
        for col in range(19):
            star_animation(star, (col * star.get_rect().width, row * star.get_rect().height))

def show_score():
    text = font.render('SCORE: {0}'.format(score), 1, (100,255,100))
    textpos = text.get_rect()
    textpos.top = 5
    textpos.left = 15
    score_surface.blit(text, textpos)

def make_a_star(size):
    star = pygame.sprite.Sprite()
    star.image = pygame.Surface((size, size))
    star.image.fill(pygame.Color(255,255,255))
    star.rect = ([100,100],(15,15))
    back_color = pygame.Color(0,0,0)
    pygame.draw.circle(star.image, back_color,(0,0),int(size/2),0)
    pygame.draw.circle(star.image, back_color,(0, size),int(size/2),0)
    pygame.draw.circle(star.image, back_color,(size,0),int(size/2),0)
    pygame.draw.circle(star.image, back_color,(size, size),int(size/2),0)
    star.image.set_colorkey(back_color)
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
    img = pygame.transform.scale(star.image, (16,16))
    img = pygame.transform.rotate(img, rotate[0])
    x_dist = (img.get_rect().width - 16)/2
    y_dist = (img.get_rect().height - 16)/2
    place.blit(img, (star.rect[0][0] - x_dist, star.rect[0][1] - y_dist))

def work():
    #print(textpos.centerx - surface.get_rect().centerx)
    if move[0]: 
        player.rect.left -= move_step
    if move[1]:
        player.rect.left += move_step
    if player.rect.left <= player_surface_rect.left:
        player.rect.left = player_surface_rect.left
    if player.rect.right >= player_surface_rect.right:
        player.rect.left = player_surface_rect.right - player.rect.width

    star_rect[0][0] += moveX(125)
    star_rect[0][1] -= moveY(125)
    #if move[2]: textpos.y -= move_step
    #if move[3]: textpos.y += move_step
    #rotate[0] += 25
    #if rotate[0] > 360: rotate[0] = 0

def display():
    game_surface.fill(pygame.Color(0,0,0))
    player_surface.fill(pygame.Color(0,0,0,0))
    Bricks.draw(game_surface)
    star_group.draw(game_surface)
    #star_animation(star, game_surface)
    player_group.draw(player_surface)
    score_surface.fill(pygame.Color(180,180,180))
    show_score()
    screen.blits(
        (
            (game_surface, game_surface_rect),
            (player_surface, player_surface_rect),
            (score_surface, score_surface_rect)
        )
    )

star = make_a_star(7)
star_rect = star.rect
star_group.add(star)
Bricks = make_bricks()
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