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

box_width = 500
box_height = 400

screen = pygame.display.set_mode((box_width,box_height),pygame.FULLSCREEN)

font = pygame.font.Font('freesansbold.ttf', 48)
font_1 = pygame.font.Font("freesansbold.ttf",24)



text = font.render('MASTERMIND', True, col_1 )
texty = font_1.render('START GAME',True,col_2)



def button():
    pygame.draw.rect(screen,col_1,(250,230,220,50))



while 1:
    screen.fill(col_3)

    screen.blit(text,(210,60))
    button()
    screen.blit(texty,(300,250))
    
    
    pygame.display.update()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            pygame.quit()

            quit()
        pygame.display.update()
