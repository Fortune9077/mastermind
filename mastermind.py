import pygame
from pygame.locals import *
import os 
'''os.environ['SDL_AUDIODRIVER'] = 'dsp' '''
import random 
import math 


pygame.init()
col_1 = (255,0,0)
col_2 = (218,165,32)
col_3 = (0,20,168)

box_width = 400
box_height = 520

screen = pygame.display.set_mode((box_width,box_height),pygame.FULLSCREEN)

font = pygame.font.Font('freesansbold.ttf', 32)

text = font.render('python on top', True, col_1 )
textRect = text.get_rect()
textRect.center = (box_width// 2, box_height // 2)


while 1:
    screen.fill(col_3)

    screen.blit(text, textRect)
    pygame.display.update()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            pygame.quit()

            quit()
        pygame.display.update()
