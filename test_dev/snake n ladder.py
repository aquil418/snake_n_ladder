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
titleboard = pygame.Surface((560,100),pygame.SRCALPHA)#making it transparent
titleboard.fill((255,255,255,80))


play_button_font = pygame.font.SysFont(None, 36)
play_button = pygame.Rect(420,350,160, 60)

font1 = pygame.font.Font('font/SunnyspellsRegular.otf',50)  
font2 = pygame.font.Font('font/Pixeltype.ttf',30)
font3 = pygame.font.Font('font/Pixeltype.ttf',55)
roll_message = font2.render("[Press Spacebar to Roll]",False,'white')
title_font = pygame.font.Font('font/SunnyspellsRegular.otf',100)
title_text = title_font.render("Snake & Ladder",False,'brown3')

menu_box = pygame.Rect(275, 175, 500, 300)
choose_text = font3.render("Select Number Of Players!",False,'red')
play_button_font = pygame.font.SysFont(None, 36)

p2box = pygame.Rect(325,295,75,75)
p3box = pygame.Rect(480,295,75,75)
p4box = pygame.Rect(635,295,75,75)
first_1_button = pygame.Rect(455,405,120,35)

#dice
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

#main loop
global state
state='first_1'

def dice_roll():
    global is_rolling, rolling_images_counter, dice_num_image, rolled_number
    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE] and is_rolling is False:
        is_rolling = True
        rand_num = random.randint(0,5)#its from the list not from the images number
        global rolled_number
        rolled_number = rand_num+1
        print("dice:",rolled_number)
        dice_num_image=dice_images[rand_num]#to take from list
        screen.blit(dice_rolling_images[rolling_images_counter], (92,520))
        rolling_images_counter+=1
        
    else:
        if is_rolling:#showing rolling animation images
            screen.blit(dice_rolling_images[rolling_images_counter], (92,520))
            rolling_images_counter +=1
            if rolling_images_counter >=8:
                is_rolling = False
                rolling_images_counter = 0
                
        else:
            screen.blit(dice_num_image, (92,520))

def first_1_screen():
    global state
    while state == 'first_1':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit() 
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.collidepoint(event.pos):
                    print("Working!Now in State first_2")
                    state = 'first_2'
                    
        screen.blit(bg_image1, (0,0))
        screen.blit(titleboard, (250,140))
        screen.blit(title_text,(275,150))
        
        mouse_pos = pygame.mouse.get_pos()
        if play_button.collidepoint(mouse_pos):
            color = (255, 255, 255)  # White when hovering box
            t_color=(0,0,0)#black text
        else:
            color = (0, 0, 0)  # Black normally
            t_color=(255,255,255)
        
        pygame.draw.rect(screen,color,play_button)
        
        play_button_text = play_button_font.render("PLAY",True,t_color)
        text_rect = play_button_text.get_rect(center=play_button.center)
        screen.blit(play_button_text, text_rect)
        
        pygame.display.update()
        
def first_2_screen():
    global state
    while state == 'first_2':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if p2box.collidepoint(event.pos):
                    print("Working!Now in State main_1")
                    state = 'main_1'
                if p3box.collidepoint(event.pos):
                    print("Working!Now in State main_2")
                    state = 'main_2'
                if p4box.collidepoint(event.pos):
                    print("Working!Now in State main_3")
                    state = 'main_3'
                if first_1_button.collidepoint(event.pos):
                    print("Back to first_1")
                    state = 'first_1'
                    
                    
        screen.blit(bg_image1,(0,0))
        pygame.draw.rect(screen, (248,248,248), menu_box)#border color
        pygame.draw.rect(screen, (155, 188, 15), menu_box.inflate(-6, -6))#inside color
        screen.blit(choose_text,(330,200))
        
        mouse_pos = pygame.mouse.get_pos()
        if p2box.collidepoint(mouse_pos):
            color2 = (255, 255, 255)#white when hovering box
            r_color='red'
        elif p3box.collidepoint(mouse_pos):
            color3 = (255, 255, 255)  # White when hovering box
            g_color='green'
        elif p4box.collidepoint(mouse_pos):
            color4 = (255, 255, 255)  # White when hovering box
            b_color='blue'
        elif first_1_button.collidepoint(mouse_pos):
            color_f = (0,0,0)
            f_color = 'white'
        else:
            color2 = (255,0,0)
            color3 = (0,128,0)
            color4 = (0,0,255)
            color_f=(255,255,255)
            r_color = 'white'
            g_color = 'white'
            b_color = 'white'
            f_color = 'black'
            
        pygame.draw.rect(screen, color2,p2box)#red 
        p2text = font3.render("2P",False,r_color)
        screen.blit(p2text,(345,320))
        
        pygame.draw.rect(screen, color3,p3box)#half the green
        p3text = font3.render("3P",False,g_color)
        screen.blit(p3text,(500,320))
        
        pygame.draw.rect(screen, color4,p4box)#blue
        p4text = font3.render("4P",False,b_color)
        screen.blit(p4text,(655,320))
        
        pygame.draw.rect(screen, color_f,first_1_button)
        first_1_button_text = font3.render("Go Back",False,f_color)
        screen.blit(first_1_button_text,(455,410))
        
        pygame.display.update()
        
while True:
    if state == 'first_1':
        first_1_screen()
    elif state == 'first_2':
        first_2_screen()
   # elif state == 'main_1':
        #dice_roll add cheyyu   
        #clock.tick(13)
