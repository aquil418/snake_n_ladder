import pygame
import sys
import random
pygame.init()

clock = pygame.time.Clock()

screen=pygame.display.set_mode((1000,650))
pygame.display.set_caption("Snake n Ladder")

bg_image1 = pygame.image.load('graphics/bgjungle2.jpg')
board_image = pygame.transform.scale(pygame.image.load('graphics/board.png'),(650,650))
menuboard = pygame.Surface((220,480),pygame.SRCALPHA)#making it transparent
menuboard.fill((255,255,255,80))
#sideboard = pygame.Rect(25, 25, 220, 480)
#diceboard = pygame.Rect(92,536,100,90)
#gameboard = pygame.Rect(250, 25, 725, 550)
font1 = pygame.font.Font('font/SunnyspellsRegular.otf',50)  
font2 = pygame.font.Font('font/Pixeltype.ttf',30)
roll_message = font2.render("[Press Spacebar to Roll]",False,'white')

dice_images = []
dice_rolling_images = []

for i in range(1,7):
    dice_image = pygame.image.load('graphics/dice/'+str(i)+'.png')
    dice_images.append(dice_image)
    
for i in range(1,9):#there are 8 rolling dice images 
    dice_rolling_image = pygame.image.load('graphics/animation/roll'+str(i)+'.png')
    dice_rolling_images.append(dice_rolling_image)
    
is_rolling = False
rolling_images_counter = 0
dice_num_image = dice_images[0]
first = True

    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 
    screen.blit(bg_image1, (0,0))
    screen.blit(roll_message,(25,625))
    screen.blit(menuboard, (25,25)) 
    #pygame.draw.rect(screen, 'darkorchid3', sideboard)
    #pygame.draw.rect(screen, 'darkorchid3', diceboard)
    #pygame.draw.rect(screen, 'darkorchid3', gameboard)
    screen.blit(board_image, (285,8))
    
    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE] and is_rolling is False:
        is_rolling = True
        rand_num = random.randint(0,5)
        dice_num_image=dice_images[rand_num]
        screen.blit(dice_rolling_images[rolling_images_counter], (92,520))
        rolling_images_counter+=1
        first = True
    else:
        if is_rolling:#showing rolling animation images
            screen.blit(dice_rolling_images[rolling_images_counter], (92,520))
            rolling_images_counter +=1
            if rolling_images_counter >=8:
                is_rolling = False
                rolling_images_counter = 0
        else:
            screen.blit(dice_num_image, (92,520))
            if first:
                first= False
                
            



    pygame.display.update()
    clock.tick(13)