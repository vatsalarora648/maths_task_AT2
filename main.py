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
BLACK=(255,0,0)
while running:
    
    for event in pygame.event.get():
        # Check if the user clicked the close button
        if event.type == pygame.QUIT:
            running = False  
    
pygame.display.update()


##game states
LEVEL_SELECTION=0
current_game_state = LEVEL_SELECTION
current_level = 1
questions_for_current_level = []
current_question_index = 0
score = 0
selected_option_index = -1 # -1 means no option selected
feedback_message = ""
feedback_color = BLACK
answer_submitted = False # To control interaction after submission

## game variables

score=0
current_game_selection=start_screen
feedback_message=0
question_for_current_level=[]

## all questions in the app
all_questions={
   #1. Advance Level 1 Year math
    [{"id": '1-1', "question": "A mysterious number is between 10 and 20. When you add 4 to this number, the result is the same as subtracting 2 from 18. What is the mysterious number?", "options": ["15", "18", "12", "10"], "answer": "12"},
        {"id": '1-2', "question": "What are the next two numbers in the sequence: 5, 8, 11, 14, ...? ", "options": ["19", "17", "15", "21"], "answer": "17"},
        {"id": '1-3', "question": "If you have 2 liters of water and you drink half a liter, how much water do you have left?", "options": ["1", "2", "5", "7"], "answer": "1"},
        {"id": '1-4', "question": "Liam has 10 cookies. He gives 3 cookies to his friend, Sarah. Then, Liam's mom gives him 5 more cookies. How many cookies does Liam have now?", "options": ["10", "7", "15", "12"], "answer": "12"},
        {"id": '1-5', "question": "A farmer has 12 chickens. He buys 6 more chickens. A fox then steals 4 chickens. How many chickens does the farmer have at the end of the day?", "options": ["14", "18", "10", "8"], "answer": "14"}
    ]
    #2. Advance Level 2 Year math
    [{"id": '1-1', "question": "A mysterious number is between 10 and 20. When you add 4 to this number, the result is the same as subtracting 2 from 18. What is the mysterious number?", "options": ["15", "18", "12", "10"], "answer": "12"},
        {"id": '1-2', "question": "What are the next two numbers in the sequence: 5, 8, 11, 14, ...? ", "options": ["19", "17", "15", "21"], "answer": "17"},
        {"id": '1-3', "question": "If you have 2 liters of water and you drink half a liter, how much water do you have left?", "options": ["1", "2", "5", "7"], "answer": "1"},
        {"id": '1-4', "question": "Liam has 10 cookies. He gives 3 cookies to his friend, Sarah. Then, Liam's mom gives him 5 more cookies. How many cookies does Liam have now?", "options": ["10", "7", "15", "12"], "answer": "12"},
        {"id": '1-5', "question": "A farmer has 12 chickens. He buys 6 more chickens. A fox then steals 4 chickens. How many chickens does the farmer have at the end of the day?", "options": ["14", "18", "10", "8"], "answer": "14"}
    ]
    #3. Advance Level 3 Year math
    [{"id": '1-1', "question": "A mysterious number is between 10 and 20. When you add 4 to this number, the result is the same as subtracting 2 from 18. What is the mysterious number?", "options": ["15", "18", "12", "10"], "answer": "12"},
        {"id": '1-2', "question": "What are the next two numbers in the sequence: 5, 8, 11, 14, ...? ", "options": ["19", "17", "15", "21"], "answer": "17"},
        {"id": '1-3', "question": "If you have 2 liters of water and you drink half a liter, how much water do you have left?", "options": ["1", "2", "5", "7"], "answer": "1"},
        {"id": '1-4', "question": "Liam has 10 cookies. He gives 3 cookies to his friend, Sarah. Then, Liam's mom gives him 5 more cookies. How many cookies does Liam have now?", "options": ["10", "7", "15", "12"], "answer": "12"},
        {"id": '1-5', "question": "A farmer has 12 chickens. He buys 6 more chickens. A fox then steals 4 chickens. How many chickens does the farmer have at the end of the day?", "options": ["14", "18", "10", "8"], "answer": "14"}
    ]
    #4. Advance Level 4 Year math
    [{"id": '1-1', "question": "A mysterious number is between 10 and 20. When you add 4 to this number, the result is the same as subtracting 2 from 18. What is the mysterious number?", "options": ["15", "18", "12", "10"], "answer": "12"},
        {"id": '1-2', "question": "What are the next two numbers in the sequence: 5, 8, 11, 14, ...? ", "options": ["19", "17", "15", "21"], "answer": "17"},
        {"id": '1-3', "question": "If you have 2 liters of water and you drink half a liter, how much water do you have left?", "options": ["1", "2", "5", "7"], "answer": "1"},
        {"id": '1-4', "question": "Liam has 10 cookies. He gives 3 cookies to his friend, Sarah. Then, Liam's mom gives him 5 more cookies. How many cookies does Liam have now?", "options": ["10", "7", "15", "12"], "answer": "12"},
        {"id": '1-5', "question": "A farmer has 12 chickens. He buys 6 more chickens. A fox then steals 4 chickens. How many chickens does the farmer have at the end of the day?", "options": ["14", "18", "10", "8"], "answer": "14"}
    ]
    #. Advance Level 5 Year math
    [{"id": '1-1', "question": "A mysterious number is between 10 and 20. When you add 4 to this number, the result is the same as subtracting 2 from 18. What is the mysterious number?", "options": ["15", "18", "12", "10"], "answer": "12"},
        {"id": '1-2', "question": "What are the next two numbers in the sequence: 5, 8, 11, 14, ...? ", "options": ["19", "17", "15", "21"], "answer": "17"},
        {"id": '1-3', "question": "If you have 2 liters of water and you drink half a liter, how much water do you have left?", "options": ["1", "2", "5", "7"], "answer": "1"},
        {"id": '1-4', "question": "Liam has 10 cookies. He gives 3 cookies to his friend, Sarah. Then, Liam's mom gives him 5 more cookies. How many cookies does Liam have now?", "options": ["10", "7", "15", "12"], "answer": "12"},
        {"id": '1-5', "question": "A farmer has 12 chickens. He buys 6 more chickens. A fox then steals 4 chickens. How many chickens does the farmer have at the end of the day?", "options": ["14", "18", "10", "8"], "answer": "14"}
    ]}

# --- Main Game Loop ---
running = True
level_buttons = []
option_rects = []
submit_button_rect = None
next_button_rect = None
play_again_button_rect = None
back_to_levels_button_rect = None

while running:
    mouse_pos = pygame.mouse.get_pos() # Get mouse position once per frame

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # Left mouse click
                if current_game_state == LEVEL_SELECTION:
                    for level_num, rect in level_buttons:
                        if rect.collidepoint(event.pos):
                            start_game_level(level_num)
                            break
                
                elif current_game_state == QUESTION_SCREEN:
                    if not answer_submitted: # Only allow selection if answer not yet submitted
                        for i, rect in enumerate(option_rects):
                            if rect.collidepoint(event.pos):
                                selected_option_index = i
                                # Visually update selected option immediately
                                current_question = questions_for_current_level[current_question_index]
                                # Re-draw screen to show selection (optional, but good for responsiveness)
                                draw_question_screen() # Call this to refresh visual state
                                break # Stop checking other options

                        if submit_button_rect and submit_button_rect.collidepoint(event.pos):
                            if selected_option_index != -1:
                                check_answer(questions_for_current_level[current_question_index], selected_option_index)
                            else:
                                feedback_message = "Please select an answer!"
                                feedback_color = RED
                                
                    elif answer_submitted and next_button_rect and next_button_rect.collidepoint(event.pos):
                        next_question()

                elif current_game_state == RESULTS_SCREEN:
                    if play_again_button_rect and play_again_button_rect.collidepoint(event.pos):
                        start_game_level(current_level) # Restart current level
                    elif back_to_levels_button_rect and back_to_levels_button_rect.collidepoint(event.pos):
                        current_game_state = LEVEL_SELECTION
                        reset_game_variables() # Reset all game progress

    # --- Drawing Logic based on Game State ---
    if current_game_state == LEVEL_SELECTION:
        level_buttons = draw_level_selection_screen() # Re-draw level buttons for hover effect
    elif current_game_state == QUESTION_SCREEN:
        option_rects, submit_button_rect, next_button_rect = draw_question_screen()
    elif current_game_state == RESULTS_SCREEN:
        play_again_button_rect, back_to_levels_button_rect = draw_results_screen()

    pygame.display.flip() # Update the full display Surface to the screen

pygame.quit()
sys.exit()