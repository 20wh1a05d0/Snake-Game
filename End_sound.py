import pygame
import random
from pygame import mixer

pygame.init()

width_screen = 500
heigth_screen = 500
screen = pygame.display.set_mode((width_screen,heigth_screen))    #to display the screen
pygame.display.set_caption("snake game!")
pygame.display.update()

x_snake = 250
y_snake = 250
width_snake = 25
heigth_snake = 25

e1_x = 0
e1_y = 0
e2_x = 0
e2_y = 0

move = 25
x_change = 0
y_change = 0

x_food = 300
y_food = 300

score = 0
level = 0
count = 0
fps = 6

snake_body = []
snake_length = 1

time = pygame.time.Clock()
pygame.display.update()

# to draw the snake
def draw_snake(snake_body,width_snake,height_snake):
    for x,y in snake_body:
        pygame.draw.rect(screen,(53, 184, 13),(x,y,width_snake,height_snake))          

    y = 25                                               #grid          #to get lines on the snake
    for i in range(23):   
        pygame.draw.line(screen,(0,0,0),(0,y),(600,y)) 
        y += 25
    x = 25    
    for i in range(23):
        pygame.draw.line(screen,(0,0,0),(x,0),(x,600))
        x += 25
    
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:              #to quit when we press cross button on the screen
            run = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            x_change = -move
            y_change = 0
            pygame.display.update()
        if event .key == pygame.K_RIGHT:
            x_change = +move
            y_change = 0
            pygame.display.update()
        if event.key == pygame.K_UP:
            y_change = -move
            x_change = 0
            pygame.display.update()
        if event.key == pygame.K_DOWN:
            y_change = +move
            x_change = 0
            pygame.display.update()
    x_snake += x_change
    y_snake += y_change
    if x_snake <= 0 or x_snake >= (width_screen-width_snake) or y_snake <= 0 or y_snake >= (heigth_screen-heigth_snake):
        fail_sound = mixer.Sound('fail.wav')
        fail_sound.play()
        run = False
        
    screen.fill((0,0,0))
    
    snake_head = []
    snake_head.append(x_snake)
    snake_head.append(y_snake)
    e1_y = y_snake + 12.5
    e2_y = y_snake + 12.5
    e1_x = x_snake + 6.25
    e2_x = x_snake + 18.75
    snake_body.append(snake_head)

    if len(snake_body) > snake_length:
        del snake_body[0]

    for x in snake_body[:-1]:
        if x == snake_head:
            fail_sound = mixer.Sound('fail.wav')
            fail_sound.play()
            run = False
        
    draw_snake(snake_body,width_snake,heigth_snake)
    e1 = pygame.draw.circle(screen,(0,0,0),(e1_x,e1_y),2.15)
    e2 = pygame.draw.circle(screen,(0,0,0),(e2_x,e2_y),2.15)
    pygame.display.update()
    
    font_style = pygame.font.SysFont("bahnschrift",25)
    text = font_style.render("score : " + str(score),True,(255,255,255))   # To create text surface object in which text is drawn,we use render() method
    text1 = font_style.render("level : " + str(level),True,(255,255,255))
    screen.blit(text,(0,0))            #blit is used to draw/write text on the screen
    screen.blit(text1,(410,0))
    pygame.display.update()

    if(x_food == x_snake and y_food == y_snake):
        score += 100
        count += 1
        x_food = random.randrange(25,475,25)# random food  #step - ?     
        y_food = random.randrange(25,475,25)  #randrange returns a randomly selected food from specified range
        snake_length += 1
        if (count % 5) == 0:
           level += 1
           fps += 2
    x_center = x_food + 12.5
    y_center = y_food + 12.5
    food = pygame.draw.circle(screen,(255,0,0),(x_center,y_center),12.5)
    pygame.display.update()

    
    time.tick(fps)
    pygame.display.update()

    
game_over = font_style.render("GAME OVER",True,(255,255,255))
screen.blit(game_over,(250,250))# to print game over
pygame.display.update()


for i in range(200): # running a empty loop
    print("")
pygame.display.update()
pygame.quit()
