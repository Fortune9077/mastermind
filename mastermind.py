import pygame
from pygame.locals import *
import os 
'''os.environ['SDL_AUDIODRIVER'] = 'dsp' '''
import random 
import math 
import sys
import tkinter
from tkinter import *
from tkinter import messagebox


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

    screen.blit(title,(180,60))
    button(230,230,220,50)
    button(230,310,220,50)
    button(230,390,220,50)

    screen.blit(start_button,(272,245))
    screen.blit(instruct_button,(253,325))
    screen.blit(exit_button,(275,405))
    
    
    pygame.display.update()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if pygame.mouse.get_pos()[0]>= 230 and pygame.mouse.get_pos()[0] <= 450:
                    if pygame.mouse.get_pos()[1]>= 230 and pygame.mouse.get_pos()[1] <=280:
                        print('START GAME')
                    if pygame.mouse.get_pos()[1]>= 310 and pygame.mouse.get_pos()[1] <= 360:
                        Tk().wm_withdraw()
                        messagebox.showinfo('Instructions','''You can only use numbers 1-7 as guesses!
                                                            You can only use each number once!
                                                            Your guess must consist of 4 numbers!
                                            If your guessed number is in the computer generated list of number but not in the right postion the computer returns WHITE
                                            If your guessed number is in the computer generated list of number and in the right postion the computer returns RED
                                            If your guessed number is not in the computer generated list the computer returns BLACK
                                            ''')                                        
                    if pygame.mouse.get_pos()[1]>= 390 and pygame.mouse.get_pos()[1] <=440:
                        pygame.quit()
                        sys.exit()
        pygame.display.update()
