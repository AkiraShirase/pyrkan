import pygame
from pygame.locals import *

pygame.init()
pygame.font.init()

move = [False, False, False, False]

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("PYRKAN")

move_step = 4

box = pygame.Rect((0,0),(400,200))
surface = pygame.Surface((400,200))
player_up_event = pygame.event.Event(pygame.USEREVENT,{'code': 'player.up'})
font = pygame.font.Font(None, 22)
text = font.render('PLAYER UP', 1, (100,255,100))
textpos = text.get_rect()
textpos.centerx = surface.get_rect().centerx

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

def work():
    #print(textpos.centerx - surface.get_rect().centerx)
    if textpos.centerx - surface.get_rect().centerx < -80 : move[0] = False
    if textpos.centerx - surface.get_rect().centerx > 80 : move[1] = False
    if move[0]: textpos.centerx -= move_step
    if move[1]: textpos.centerx += move_step
    if move[2]: textpos.y -= move_step
    if move[3]: textpos.y += move_step

def display():
    surface.fill(pygame.Color(200,0,0))
    surface.blit(text, textpos)
    screen.blit(surface,(0,0))

pygame.time.set_timer(USEREVENT + 1, 18)
while 1:
    for event in pygame.event.get():
        if event.type == QUIT: quit()
        elif event.type == KEYDOWN: press_key(event.key)
        elif event.type == KEYUP: release_key(event.key)
        elif event.type == USEREVENT: process_user_event(event.code)
        elif event.type == USEREVENT + 1: 
            work()
            display()
            pygame.display.flip()