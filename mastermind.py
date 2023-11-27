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



title = font.render('MASTERMIND', True, col_1 )
start_button = font_1.render('START GAME',True,col_2)
instruct_button = font_1.render('INSTRUCTIONS',True, col_2)
exit_button = font_1.render('EXIT GAME',True,col_2 )



def button(x,y,w,h):
    pygame.draw.rect(screen,col_1,(x,y,w,h))



while 1:
    screen.fill(col_3)

    screen.blit(title,(210,60))
    button(250,230,220,50)
    button(250,310,220,50)
    button(250,390,220,50)

    screen.blit(start_button,(300,250))
    screen.blit(instruct_button,(300,330))
    screen.blit(exit_button,(300,410))
    
    
    pygame.display.update()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if pygame.mouse.get_pos()[0]>= 250 and pygame.mouse.get_pos()[0] <= 470:
                    print(" Button range!")
                
        pygame.display.update()
