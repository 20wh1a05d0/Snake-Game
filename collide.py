import pygame
import random

pygame.init()

width_screen = 500
heigth_screen = 500
screen = pygame.display.set_mode((width_screen,heigth_screen),flags = 0)
pygame.display.set_caption("snake game!")
pygame.display.update()

x_snake = 250
y_snake = 250
width_snake = 25
heigth_snake = 25

move = 25
x_change = 0
y_change = 0

x_food = 300
y_food = 300

score = 0
level = 0
count = 0

snake_body = []
snake_length = 1

time = pygame.time.Clock()
pygame.display.update()

# to draw the snake
def draw_snake(snake_body,width_snake,height_snake):
    for x,y in snake_body:
        pygame.draw.rect(screen,(53, 184, 13),(x,y,width_snake,height_snake))

    y = 25
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
        if event.type == pygame.QUIT:
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
        run = False
        
    screen.fill((0,0,0))
    
    snake_head = []
    snake_head.append(x_snake)
    snake_head.append(y_snake)
    snake_body.append(snake_head)

    if len(snake_body) > snake_length:
        del snake_body[0]

    for x in snake_body[:-1]:
        if x == snake_head:
            run = False
        
    draw_snake(snake_body,width_snake,heigth_snake)
    pygame.display.update()
    font_style = pygame.font.SysFont("bahnschrift",25)
    text = font_style.render("score : " + str(score),True,(255,255,255))
    text1 = font_style.render("level : " + str(level),True,(255,255,255))
    screen.blit(text,(0,0))
    screen.blit(text1,(410,0))
    pygame.display.update()

    
    if(x_food == x_snake and y_food == y_snake):
        score += 100
        count += 1
        x_food = random.randrange(25,475,25)# random food 
        y_food = random.randrange(25,475,25)
        snake_length += 1
        if (count % 5) == 0:
           level += 1
    x_center = x_food + 12.5
    y_center = y_food + 12.5
    food = pygame.draw.circle(screen,(255,0,0),(x_center,y_center),12.5)
    pygame.display.update()

    
    time.tick(6)
    pygame.display.update()

    
game_over = font_style.render("GAME OVER",True,(255,255,255))
screen.blit(game_over,(250,250))# to print game over
pygame.display.update()


for i in range(200): # running a empty loop
    print("")
pygame.display.update()
pygame.quit()
