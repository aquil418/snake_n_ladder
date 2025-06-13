import pygame
import sys
import random
pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((1000, 650))
pygame.display.set_caption("Snake n Ladder")

bg_image1 = pygame.image.load('graphics/bgjungle2.jpg')
board_image = pygame.transform.scale(pygame.image.load('graphics/board.png'), (650, 650))

font1 = pygame.font.Font('font/SunnyspellsRegular.otf', 50)
font2 = pygame.font.Font('font/Pixeltype.ttf', 30)
font3 = pygame.font.Font('font/Pixeltype.ttf', 55)
title_font = pygame.font.Font('font/SunnyspellsRegular.otf', 100)

roll_message = font2.render("[Press Spacebar to Roll]", False, 'white')
title_text = title_font.render("Snake & Ladder", False, 'brown3')

menuboard = pygame.Surface((220, 480), pygame.SRCALPHA)
menuboard.fill((255, 255, 255, 80))
titleboard = pygame.Surface((560, 100), pygame.SRCALPHA)
titleboard.fill((255, 255, 255, 80))

#Dice
dice_images = [pygame.image.load(f'graphics/dice/{i}.png') for i in range(1, 7)]
dice_rolling_images = [pygame.image.load(f'graphics/animation/roll{i}.png') for i in range(1, 9)]
dice_num_image = dice_images[0]
is_rolling = False
rolling_images_counter = 0
rolled_number = 1

#Game State
state = 'first_1'
players = []
current_player_index = 0
moving = False
target_tile = 0
move_timer = 0
move_delay = 10

#Board Layout
cell_size = 65
start_x = 285
start_y = 8

def get_pos(tile_num):
    row = tile_num // 10
    col = tile_num % 10
    if row % 2 == 0:
        x = start_x + col * cell_size
    else:
        x = start_x + (9 - col) * cell_size
    y = start_y + (9 - row) * cell_size
    return x + cell_size // 2, y + cell_size // 2

#Snakes n ladders
snakes_ladders = {
    2: 17, 5:66, 11:28, 27:3, 32:47,
    41:20, 55:24, 68:29, 75:84,79:37,
    85:46, 96:54
}

#Buttons
play_button = pygame.Rect(420, 350, 160, 60)
menu_box = pygame.Rect(275, 175, 500, 300)
p2box = pygame.Rect(325, 295, 75, 75)
p3box = pygame.Rect(480, 295, 75, 75)
p4box = pygame.Rect(635, 295, 75, 75)
first_1_button = pygame.Rect(455, 405, 120, 35)

def roll_dice():
    global is_rolling, rolling_images_counter, dice_num_image, rolled_number, target_tile, moving
    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE] and not is_rolling and not moving:
        is_rolling = True
        rolled_number = random.randint(1, 6)
        dice_num_image = dice_images[rolled_number - 1]
        print(f"Player {current_player_index + 1} rolled: {rolled_number}")

    if is_rolling:
        screen.blit(dice_rolling_images[rolling_images_counter], (92, 520))
        rolling_images_counter += 1
        if rolling_images_counter >= 8:
            is_rolling = False
            rolling_images_counter = 0
            player = players[current_player_index]
            target_tile = min(player['tile'] + rolled_number, 99)
            moving = True
    else:
        screen.blit(dice_num_image, (92, 520))

def draw_players():
    for player in players:
        x, y = get_pos(player['tile'])
        pygame.draw.circle(screen, player['color'], (x, y), 8)

def update_player():
    global moving, move_timer, current_player_index, state
    if moving:
        move_timer += 1
        if move_timer >= move_delay:
            player = players[current_player_index]
            if player['tile'] < target_tile:
                player['tile'] += 1
            elif player['tile'] == target_tile:
                # Handle snake and ladder after reaching the target tile
                if player['tile'] in snakes_ladders:
                    player['tile'] = snakes_ladders[player['tile']]  # Update tile based on snakes or ladders
                    print(f"Player {current_player_index + 1} hit a snake/ladder!")

                # Check if the player has won
                if player['tile'] == 99:  # Player has won
                    display_winner(current_player_index)
                    state = 'first_1'  # Reset to the first screen after showing the winner
                    return

                moving = False
                current_player_index = (current_player_index + 1) % len(players)  # Move to next player
            move_timer = 0

def display_winner(winner_index):
    winner_text = font1.render(f"Player {winner_index + 1} Wins!", True, 'green')
    back_button = pygame.Rect(400, 350, 200, 50)
    
    while True:
        screen.fill((0, 0, 0))  # Fill screen with black to highlight the box
        screen.blit(winner_text, (350, 200))
        
        # Draw menu box and back button
        pygame.draw.rect(screen, (255, 255, 255), back_button)
        back_button_text = font2.render("Back to Menu", True, 'black')
        screen.blit(back_button_text, (back_button.x + 45, back_button.y + 10))

        # Event handling for the button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(event.pos):
                    return  # Return to the 'first_1' state
        
        pygame.display.update()

def first_1_screen():
    global state
    while state == 'first_1':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.collidepoint(event.pos):
                    state = 'first_2'

        screen.blit(bg_image1, (0, 0))
        screen.blit(titleboard, (250, 140))
        screen.blit(title_text, (275, 150))
        mouse_pos = pygame.mouse.get_pos()
        color = (255, 255, 255) if play_button.collidepoint(mouse_pos) else (0, 0, 0)
        t_color = (0, 0, 0) if play_button.collidepoint(mouse_pos) else (255, 255, 255)
        pygame.draw.rect(screen, color, play_button)
        play_button_text = pygame.font.SysFont(None, 36).render("PLAY", True, t_color)
        text_rect = play_button_text.get_rect(center=play_button.center)
        screen.blit(play_button_text, text_rect)
        pygame.display.update()

def first_2_screen():
    global state, players
    while state == 'first_2':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if p2box.collidepoint(event.pos):
                    players = [ {'color': (200, 0, 0), 'tile': 0}, {'color': (0, 0, 255), 'tile': 0} ]
                    state = 'main_1'
                elif p3box.collidepoint(event.pos):
                    players = [ {'color': (200, 0, 0), 'tile': 0}, {'color': (0, 0, 255), 'tile': 0}, {'color': (0, 255, 0), 'tile': 0} ]
                    state = 'main_1'
                elif p4box.collidepoint(event.pos):
                    players = [ {'color': (200, 0, 0), 'tile': 0}, {'color': (0, 0, 255), 'tile': 0}, {'color': (0, 255, 0), 'tile': 0}, {'color': (255, 255, 0), 'tile': 0} ]
                    state = 'main_1'
                elif first_1_button.collidepoint(event.pos):
                    state = 'first_1'

        screen.blit(bg_image1, (0, 0))
        pygame.draw.rect(screen, (248, 248, 248), menu_box)
        pygame.draw.rect(screen, (155, 188, 15), menu_box.inflate(-6, -6))
        screen.blit(font3.render("Select Number Of Players!", False, 'red'), (330, 200))

        mouse_pos = pygame.mouse.get_pos()
        def box_state(rect, hover_color, base_color, text):
            color = hover_color if rect.collidepoint(mouse_pos) else base_color
            text_color = 'black' if rect.collidepoint(mouse_pos) else 'white'
            pygame.draw.rect(screen, color, rect)
            screen.blit(font3.render(text, False, text_color), (rect.x + 20, rect.y + 25))
        box_state(p2box, (255, 255, 255), (255, 0, 0), "2P")
        box_state(p3box, (255, 255, 255), (0, 128, 0), "3P")
        box_state(p4box, (255, 255, 255), (0, 0, 255), "4P")
        box_state(first_1_button, (0, 0, 0), (255, 255, 255), "Back")
        
        
        pygame.display.update()

def main_game():
    global state
    while state == 'main_1':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.blit(bg_image1, (0, 0))
        screen.blit(roll_message, (25, 625))
        screen.blit(menuboard, (25, 25))
        screen.blit(board_image, (285, 8))
        menu_text1 = font2.render("Ladders take you up", True, 'black')
        menu_text2 = font2.render("Snakes will devour you", True, 'black')
        menu_text3 = font2.render("and will take you down!", True, 'black')
        menu_text4 = font2.render("Whoever reaches finish", True, 'navyblue')
        menu_text5 = font2.render("shall be the winner!!", True, 'navyblue')
        screen.blit(menu_text1, (35, 100))  
        screen.blit(menu_text2, (35, 130)) 
        screen.blit(menu_text3, (35, 160))
        screen.blit(menu_text4, (35, 220))
        screen.blit(menu_text5, (35, 250))
        
        draw_players()
        roll_dice()
        update_player()
        pygame.display.update()
        clock.tick(60)

# === Game Loop ===
while True:
    if state == 'first_1':
        first_1_screen()
    elif state == 'first_2':
        first_2_screen()
    elif state == 'main_1':
        main_game()
