
import pygame
import random
import sys

# --- Pygame Initialization ---
pygame.init()

# --- Screen Dimensions ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Math Whiz Challenge")

# --- Colors (RGB) ---
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 123, 255)
GREEN = (40, 167, 69)
RED = (220, 53, 69)
LIGHT_GRAY = (236, 240, 241)
DARK_GRAY = (52, 73, 94)
ACCENT_BLUE = (91, 192, 222) # For level buttons
HOVER_BLUE = (51, 122, 183)

# --- Fonts ---
FONT_XL = pygame.font.Font(None, 74) # For main titles
FONT_LG = pygame.font.Font(None, 48) # For questions
FONT_MD = pygame.font.Font(None, 36) # For options, feedback
FONT_SM = pygame.font.Font(None, 28) # For score

# --- Game States ---
LEVEL_SELECTION = 0
QUESTION_SCREEN = 1
RESULTS_SCREEN = 2

# --- Game Variables ---
current_game_state = LEVEL_SELECTION
current_level = 1
questions_for_current_level = []
current_question_index = 0
score = 0
selected_option_index = -1 # -1 means no option selected
feedback_message = ""
feedback_color = BLACK
answer_submitted = False # To control interaction after submission

# --- Question Data ---
# Structure: {level_number: [{id, question, options, answer}, ...]}
ALL_QUESTIONS = {
    1: [ # Level 1: Year 1 Math (Addition up to 10, simple counting)
        {"id": '1-1', "question": "What is 5 + 3?", "options": ["7", "8", "9", "10"], "answer": "8"},
        {"id": '1-2', "question": "Count the shapes: 2 + 4?", "options": ["5", "6", "7", "8"], "answer": "6"},
        {"id": '1-3', "question": "If you have 3 apples and get 2 more, how many do you have?", "options": ["4", "5", "6", "7"], "answer": "5"},
        {"id": '1-4', "question": "What is 10 - 6?", "options": ["3", "4", "5", "6"], "answer": "4"},
        {"id": '1-5', "question": "Which number comes after 7?", "options": ["6", "8", "9", "10"], "answer": "8"}
    ],
    2: [ # Level 2: Year 2 Math (Addition/Subtraction up to 20, simple patterns)
        {"id": '2-1', "question": "What is 12 + 7?", "options": ["18", "19", "20", "21"], "answer": "19"},
        {"id": '2-2', "question": "Subtract 9 from 15.", "options": ["5", "6", "7", "8"], "answer": "6"},
        {"id": '2-3', "question": "If a pack has 10 cookies and you eat 3, how many are left?", "options": ["6", "7", "8", "9"], "answer": "7"},
        {"id": '2-4', "question": "What is the next number in the pattern: 2, 4, 6, 8, __?", "options": ["9", "10", "11", "12"], "answer": "10"},
        {"id": '2-5', "question": "Double 8 is...?", "options": ["14", "15", "16", "17"], "answer": "16"}
    ],
    3: [ # Level 3: Year 3 Math (Multiplication/Division basics, larger numbers)
        {"id": '3-1', "question": "What is 4 multiplied by 6?", "options": ["20", "22", "24", "26"], "answer": "24"},
        {"id": '3-2', "question": "Divide 28 by 7.", "options": ["3", "4", "5", "6"], "answer": "4"},
        {"id": '3-3', "question": "A box holds 8 pencils. How many pencils are in 5 boxes?", "options": ["35", "40", "45", "50"], "answer": "40"},
        {"id": '3-4', "question": "What is 35 + 27?", "options": ["60", "61", "62", "63"], "answer": "62"},
        {"id": '3-5', "question": "How many cents in a dollar?", "options": ["10", "50", "100", "1000"], "answer": "100"}
    ],
    4: [ # Level 4: Year 4 Math (Fractions, decimals, multi-step problems)
        {"id": '4-1', "question": "What is 1/2 of 50?", "options": ["20", "25", "30", "35"], "answer": "25"},
        {"id": '4-2', "question": "Convert 0.75 into a fraction.", "options": ["1/2", "3/4", "1/4", "7/10"], "answer": "3/4" },
        {"id": '4-3', "question": "If a shirt costs $24 and is on sale for half price, what is the new price?", "options": ["$10", "$12", "$14", "$16"], "answer": "$12"},
        {"id": '4-4', "question": "What is 150 divided by 3?", "options": ["40", "45", "50", "55"], "answer": "50"},
        {"id": '4-5', "question": "Add: 2.5 + 3.7", "options": ["5.2", "6.2", "6.0", "5.7"], "answer": "6.2"}
    ],
    5: [ # Level 5: Year 5 Math (More complex operations, geometry, larger numbers)
        {"id": '5-1', "question": "What is 12 x 11?", "options": ["121", "132", "144", "110"], "answer": "132"},
        {"id": '5-2', "question": "A rectangle has a length of 8 cm and a width of 5 cm. What is its area?", "options": ["13 cm²", "26 cm²", "40 cm²", "30 cm²"], "answer": "40 cm²"},
        {"id": '5-3', "question": "What is the decimal equivalent of 3/5?", "options": ["0.3", "0.5", "0.6", "0.7"], "answer": "0.6"},
        {"id": '5-4', "question": "Calculate: (15 + 5) ÷ 4", "options": ["4", "5", "6", "7"], "answer": "5"},
        {"id": '5-5', "question": "If you start with 200, subtract 50, then add 30, what number do you have?", "options": ["170", "180", "190", "200"], "answer": "180"}
    ]
}

# --- Helper Functions for Drawing ---
def draw_text(surface, text, font, color, x, y, center_x=False):
    text_surface = font.render(text, True, color)
    if center_x:
        text_rect = text_surface.get_rect(center=(x, y))
    else:
        text_rect = text_surface.get_rect(topleft=(x, y))
    surface.blit(text_surface, text_rect)
    return text_rect # Return rect for click detection

def draw_button(surface, rect, text, font, button_color, text_color, hover_color=None, mouse_pos=None):
    if hover_color and mouse_pos and rect.collidepoint(mouse_pos):
        pygame.draw.rect(surface, hover_color, rect, border_radius=8)
    else:
        pygame.draw.rect(surface, button_color, rect, border_radius=8)
    
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=rect.center)
    surface.blit(text_surface, text_rect)
    return rect # Return the rect for event handling

# --- Game Logic Functions ---

def reset_game_variables():
    global current_question_index, score, selected_option_index, feedback_message, feedback_color, answer_submitted
    current_question_index = 0
    score = 0
    selected_option_index = -1
    feedback_message = ""
    feedback_color = BLACK
    answer_submitted = False

def start_game_level(level):
    global current_game_state, current_level, questions_for_current_level
    current_level = level
    questions_for_current_level = ALL_QUESTIONS[level][:] # Create a copy
    random.shuffle(questions_for_current_level) # Shuffle questions for the level
    reset_game_variables()
    current_game_state = QUESTION_SCREEN

def load_current_question():
    global selected_option_index, feedback_message, feedback_color, answer_submitted
    selected_option_index = -1
    feedback_message = ""
    feedback_color = BLACK
    answer_submitted = False

def check_answer(question, option_index):
    global score, feedback_message, feedback_color, answer_submitted
    if answer_submitted: # Prevent double submission
        return

    selected_answer = question["options"][option_index]
    
    if selected_answer == question["answer"]:
        score += 1
        feedback_message = "Correct! Well done!"
        feedback_color = GREEN
    else:
        feedback_message = f"Incorrect. The correct answer was {question['answer']}."
        feedback_color = RED
    answer_submitted = True

def next_question():
    global current_question_index, current_game_state
    current_question_index += 1
    if current_question_index >= len(questions_for_current_level):
        current_game_state = RESULTS_SCREEN
    else:
        load_current_question()

# --- Drawing Functions for Each Screen ---

def draw_level_selection_screen():
    SCREEN.fill(LIGHT_GRAY)
    draw_text(SCREEN, "Math Whiz Challenge", FONT_XL, DARK_GRAY, SCREEN_WIDTH // 2, 100, center_x=True)
    draw_text(SCREEN, "Select Your Level", FONT_LG, DARK_GRAY, SCREEN_WIDTH // 2, 200, center_x=True)

    button_y_start = 280
    button_spacing = 80
    button_width = 200
    button_height = 60
    
    level_buttons = []
    for i in range(1, 6): # Levels 1 to 5
        rect = pygame.Rect(SCREEN_WIDTH // 2 - button_width // 2, button_y_start + (i - 1) * button_spacing, button_width, button_height)
        level_buttons.append((i, rect)) # Store level number and its rect
        draw_button(SCREEN, rect, f"Level {i}", FONT_MD, ACCENT_BLUE, WHITE, HOVER_BLUE, pygame.mouse.get_pos())
    return level_buttons # Return button rects for click detection

def draw_question_screen():
    SCREEN.fill(LIGHT_GRAY)
    
    # Header
    draw_text(SCREEN, f"Level {current_level} Math", FONT_LG, DARK_GRAY, SCREEN_WIDTH // 2, 50, center_x=True)
    draw_text(SCREEN, f"Score: {score} / {current_question_index}", FONT_SM, DARK_GRAY, 50, 50) # Left aligned score

    # Question
    current_question = questions_for_current_level[current_question_index]
    draw_text(SCREEN, current_question["question"], FONT_LG, BLACK, SCREEN_WIDTH // 2, 200, center_x=True)

    # Options
    option_rects = []
    option_y_start = 300
    option_height = 60
    option_spacing = 20
    option_width = 300
    
    for i, option in enumerate(current_question["options"]):
        rect = pygame.Rect(SCREEN_WIDTH // 2 - option_width // 2, option_y_start + i * (option_height + option_spacing), option_width, option_height)
        
        button_color = LIGHT_GRAY
        text_color = DARK_GRAY
        hover_color = WHITE
        
        if selected_option_index == i:
            button_color = BLUE # Selected color
            text_color = WHITE
            hover_color = BLUE # Keep selected color on hover

        if answer_submitted:
            if current_question["options"][i] == current_question["answer"]:
                button_color = GREEN # Correct answer highlighted
                text_color = WHITE
            elif i == selected_option_index and current_question["options"][i] != current_question["answer"]:
                button_color = RED # Incorrect selected answer
                text_color = WHITE
            hover_color = button_color # No hover effect after submitted

        draw_button(SCREEN, rect, option, FONT_MD, button_color, text_color, hover_color, pygame.mouse.get_pos() if not answer_submitted else None)
        option_rects.append(rect)

    # Feedback message
    draw_text(SCREEN, feedback_message, FONT_MD, feedback_color, SCREEN_WIDTH // 2, SCREEN_HEIGHT - 120, center_x=True)

    # Submit/Next Button
    button_width = 200
    button_height = 60
    button_y = SCREEN_HEIGHT - 70
    submit_rect = pygame.Rect(SCREEN_WIDTH // 2 - button_width // 2, button_y, button_width, button_height)

    if not answer_submitted:
        submit_button_drawn = draw_button(SCREEN, submit_rect, "Submit Answer", FONT_MD, GREEN, WHITE, (35, 139, 56), pygame.mouse.get_pos())
        next_button_drawn = None
    else:
        submit_button_drawn = None # Button is hidden
        next_button_drawn = draw_button(SCREEN, submit_rect, "Next Question", FONT_MD, BLUE, WHITE, (0, 86, 179), pygame.mouse.get_pos())

    return option_rects, submit_button_drawn, next_button_drawn

def draw_results_screen():
    SCREEN.fill(LIGHT_GRAY)
    draw_text(SCREEN, "Level Complete!", FONT_XL, DARK_GRAY, SCREEN_WIDTH // 2, 100, center_x=True)
    draw_text(SCREEN, f"You scored: {score} out of {len(questions_for_current_level)}", FONT_LG, BLACK, SCREEN_WIDTH // 2, 250, center_x=True)

    button_width = 250
    button_height = 60
    
    play_again_rect = pygame.Rect(SCREEN_WIDTH // 2 - button_width // 2, 400, button_width, button_height)
    back_to_levels_rect = pygame.Rect(SCREEN_WIDTH // 2 - button_width // 2, 480, button_width, button_height)

    play_again_button_drawn = draw_button(SCREEN, play_again_rect, "Play Again", FONT_MD, ACCENT_BLUE, WHITE, HOVER_BLUE, pygame.mouse.get_pos())
    back_to_levels_button_drawn = draw_button(SCREEN, back_to_levels_rect, "Back to Levels", FONT_MD, DARK_GRAY, WHITE, (80, 80, 80), pygame.mouse.get_pos())
    
    return play_again_button_drawn, back_to_levels_button_drawn

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
