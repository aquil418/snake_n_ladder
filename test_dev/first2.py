import pygame
import sys

pygame.init()

screen=pygame.display.set_mode((1000,650))
pygame.display.set_caption("first_2")

bg_image1 = pygame.image.load('graphics/bgjungle2.jpg')
font3 = pygame.font.Font('font/Pixeltype.ttf',55)

menu_box = pygame.Rect(275, 175, 500, 300)
choose_text = font3.render("Select Number Of Players!",False,'red')
p2box = pygame.Rect(325,295,75,75)

p3box = pygame.Rect(480,295,75,75)

p4box = pygame.Rect(635,295,75,75)

first_1_button = pygame.Rect(455,405,120,35)


while True:
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
                state = "first_1"
                
                
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