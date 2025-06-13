import pygame
import sys

pygame.init()

screen=pygame.display.set_mode((1000,650))
pygame.display.set_caption("first_1")

bg_image1 = pygame.image.load('graphics/bgjungle2.jpg')


title_font = pygame.font.Font('font/SunnyspellsRegular.otf',100)
title_text = title_font.render("Snake & Ladder",False,'brown3')

play_button_font = pygame.font.SysFont(None, 36)
play_button = pygame.Rect(420,350,160, 60)

titleboard = pygame.Surface((560,100),pygame.SRCALPHA)#making it transparent
titleboard.fill((255,255,255,80))

state='first_1'

while True:
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