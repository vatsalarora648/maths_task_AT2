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
   #1. Advance Level 1 Year math
    {"id": '1-1', "question": "A mysterious number is between 10 and 20. When you add 4 to this number, the result is the same as subtracting 2 from 18. What is the mysterious number?", "options": ["15", "18", "12", "10"], "answer": "12"},
        {"id": '1-2', "question": "Count the shapes: 2 + 4?", "options": ["5", "6", "7", "8"], "answer": "6"},
        {"id": '1-3', "question": "If you have 3 apples and get 2 more, how many do you have?", "options": ["4", "5", "6", "7"], "answer": "5"},
        {"id": '1-4', "question": "What is 10 - 6?", "options": ["3", "4", "5", "6"], "answer": "4"},
        {"id": '1-5', "question": "Which number comes after 7?", "options": ["6", "8", "9", "10"], "answer": "8"}
}
#def start_screen():
    