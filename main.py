import pygame
#import random 
#import sys


## pygame display window
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Maths")
running = True

while running:
    
    for event in pygame.event.get():
        # Check if the user clicked the close button
        if event.type == pygame.QUIT:
            running = False  
    
pygame.display.update()


##game states
start_screen=0
question_screen=1
result_screen=2

## game variables

score=0
current_game_selection=start_screen
feedback_message=0
question_for_current_level=[]


all_questtions={
   1. Advance Level 1 Year math
}
#def start_screen():
    