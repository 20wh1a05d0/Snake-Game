import pygame
import random
pygame.init()
width_screen = 500
heigth_screen = 500
screen = pygame.display.set_mode((width_screen,heigth_screen))
pygame.display.set_caption("snake game!")
pygame.display.update()
x_snake = 250
y_snake = 250
width_snake = 25
heigth_snake = 25
speed = 25
x_food = 300
y_food = 300
score = 0

time = pygame.time.Clock()
pygame.display.update()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            x_snake -= speed
            if x_snake <= 0:
                run = False
                print("game over")
            pygame.display.update()
        elif event.key == pygame.K_RIGHT:
           x_snake += speed
           if x_snake >= width_screen - width_snake:
               run = False
               print("game over")
           pygame.display.update()
        elif event.key == pygame.K_UP:
            y_snake -= speed
            if y_snake <= 0:
                run = False
                print("game over")
            pygame.display.update()
        elif event.key == pygame.K_DOWN:
            y_snake += speed
            if y_snake >= heigth_screen - heigth_snake:
                run = False
                print("game over")
            pygame.display.update()
    screen.fill((0,0,0))
    y = 25
    for i in range(19):
        pygame.draw.line(screen,(0,0,0),(0,y),(500,y)) 
        y += 25
    x = 25    
    for i in range(19):
        pygame.draw.line(screen,(0,0,0),(x,0),(x,500))
        x += 25
    pygame.display.update()     
    snake = pygame.draw.rect(screen,(0,0,255),(x_snake,y_snake,width_snake,heigth_snake))
    if(x_food == x_snake and y_food == y_snake):
        #heigth_snake += 25
        score += 100
        x_food = random.randrange(25,475,25)
        y_food = random.randrange(25,475,25)
    food = pygame.draw.rect(screen,(255,0,0),(x_food,y_food,25,25))
    pygame.display.update()  
    time.tick(10)
    pygame.display.update()
pygame.display.update()
pygame.quit()
