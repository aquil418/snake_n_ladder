import pygame
import sys
import random

pygame.init()
screen = pygame.display.set_mode((1000, 650))
pygame.display.set_caption("Snake n Ladder")
clock = pygame.time.Clock()

# --- Assets ---
bg_image = pygame.image.load('graphics/bgjungle2.jpg')
board_image = pygame.transform.scale(pygame.image.load('graphics/board.png'), (650, 650))
menuboard = pygame.Surface((220, 480), pygame.SRCALPHA)
menuboard.fill((255, 255, 255, 80))

font1 = pygame.font.Font('font/SunnyspellsRegular.otf', 50)
font2 = pygame.font.Font('font/Pixeltype.ttf', 30)
roll_message = font2.render("[Press Spacebar to Roll]", False, 'white')

# --- Dice ---
dice_images = [pygame.image.load(f'graphics/dice/{i}.png') for i in range(1, 7)]
dice_rolling_images = [pygame.image.load(f'graphics/animation/roll{i}.png') for i in range(1, 9)]
is_rolling = False
rolling_images_counter = 0
dice_num_image = dice_images[0]
rolled_number = 0

# --- Snakes and Ladders ---
snakes = {97: 55, 86: 47, 80: 38, 69: 30, 56: 25, 42: 21, 28: 4}
ladders = {3: 18, 6: 67, 12: 29, 33: 48, 58: 82, 76: 85}

# --- Player Data ---
player_colors = [(255, 0, 0), (0, 0, 255)]
player_positions = [1, 1]
current_player = 0
moving = False
move_path = []


def get_coordinates(position):
    if position < 1:
        position = 1
    elif position > 100:
        position = 100
    row = (position - 1) // 10
    col = (position - 1) % 10 if row % 2 == 0 else 9 - (position - 1) % 10
    x = 285 + col * 65 + 32
    y = 8 + (9 - row) * 65 + 32
    return x, y


def prepare_movement(player_index, steps):
    global moving, move_path
    current = player_positions[player_index]
    move_path = [current + i for i in range(1, steps + 1)]
    moving = True


def apply_snakes_and_ladders(pos):
    if pos in snakes:
        return snakes[pos]
    elif pos in ladders:
        return ladders[pos]
    return pos


def roll_dice():
    global is_rolling, rolling_images_counter, dice_num_image, rolled_number
    is_rolling = True
    rolling_images_counter = 0
    rolled_number = random.randint(1, 6)
    dice_num_image = dice_images[rolled_number - 1]
    prepare_movement(current_player, rolled_number)


def update_movement():
    global moving, current_player
    if move_path:
        player_positions[current_player] = move_path.pop(0)
    else:
        # Check snake or ladder
        player_positions[current_player] = apply_snakes_and_ladders(player_positions[current_player])
        if player_positions[current_player] == 100:
            print(f"Player {current_player + 1} wins!")
        else:
            switch_turn()
        moving = False


def switch_turn():
    global current_player
    current_player = (current_player + 1) % len(player_positions)


# --- Main Game Loop ---
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not is_rolling and not moving:
            roll_dice()

    screen.blit(bg_image, (0, 0))
    screen.blit(board_image, (285, 8))
    screen.blit(menuboard, (25, 25))
    screen.blit(roll_message, (25, 625))

    # Dice animation or number
    if is_rolling:
        if rolling_images_counter < len(dice_rolling_images):
            screen.blit(dice_rolling_images[rolling_images_counter], (92, 520))
            rolling_images_counter += 1
        else:
            is_rolling = False
            screen.blit(dice_num_image, (92, 520))
    else:
        screen.blit(dice_num_image, (92, 520))

    if moving:
        update_movement()

    for idx, pos in enumerate(player_positions):
        x, y = get_coordinates(pos)
        pygame.draw.circle(screen, player_colors[idx], (x, y), 10)

    pygame.display.update()
    clock.tick(30)