import pygame
import random
from pygame import mixer

pygame.init()
pygame.font.init()
pygame.mixer.init()

#Creating the screen
width_screen = 500
heigth_screen = 500
screen = pygame.display.set_mode((width_screen,heigth_screen))
pygame.display.set_caption("Snake game!")
pygame.display.update()

#Displaying Home screen
font_style1 = pygame.font.SysFont("Arial Black",35)
image = pygame.image.load('homepage1.jpg')
screen.blit(image,(0,0))
pygame.display.update()
start = font_style1.render("Hit Space bar to START",True,(0,0,0))
screen.blit(start,(25 ,100))
pygame.display.update()

#To draw the snake
def draw_snake(snake_body,width_snake,height_snake):
    for x,y in snake_body:
        pygame.draw.rect(screen,(53, 184, 13),(x,y,width_snake,height_snake))
    y = 25
    for i in range(19):
        pygame.draw.line(screen,(0,0,0),(0,y),(500,y)) 
        y += 25
    x = 25    
    for i in range(19):
        pygame.draw.line(screen,(0,0,0),(x,0),(x,500))
        x += 25

#Main Game loop
def game_loop():
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
	fps = 5

	snake_body = []
	snake_length = 1

	time = pygame.time.Clock()
	pygame.display.update()
	
	run = True
	game_over = False
	while run:
		while game_over:
		    #To print game over
			font_style2 = pygame.font.SysFont("bahnschrift",25)
			font_style1 = pygame.font.SysFont("Arial Black",35)
			game_over = font_style1.render("GAME OVER!!!",True,(255,0,0))
			cont = font_style2.render("Press C to CONTINUE",True,(0,0,0))
			quit = font_style2.render("Press Q to QUIT",True,(0,0,0))
			screen.fill((50,205,50))
			screen.blit(game_over,(105,100))
			screen.blit(cont,(125,250))
			screen.blit(quit,(150,300))
			pygame.display.update()

			#Continue & Quit options
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						pygame.quit()
					if event.key == pygame.K_c:
						game_loop()

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
		
		#Setting Boundaries
		if x_snake <= 0 or x_snake >= (width_screen - width_snake) or y_snake <= 0 or y_snake >= (heigth_screen - heigth_snake):
			fail_sound = mixer.Sound('fail.wav')
			fail_sound.play()
			game_over = True
			
		screen.fill((0,0,0))
			
		snake_head = []
		snake_head.append(x_snake)
		snake_head.append(y_snake)
		#Eyes of the snake
		e1_x = x_snake + 6.25
		e1_y = y_snake + 12.25
		e2_x = x_snake + 18.25
		e2_y = y_snake + 12.25
		snake_body.append(snake_head)

		if len(snake_body) > snake_length:
			del snake_body[0]
			
		#Snake intersecting itself
		for a in snake_body[:-1]:
			if a == snake_head:
				fail_sound = mixer.Sound('fail.wav')
				fail_sound.play()
				game_over = True
		pygame.display.update()
		
			
		draw_snake(snake_body,width_snake,heigth_snake)
		pygame.draw.circle(screen,(0,0,0),(e1_x,e1_y),2.15)
		pygame.draw.circle(screen,(0,0,0),(e2_x,e2_y),2.15)
		pygame.display.update()
		
		#Displaying Score & Level
		font_style = pygame.font.SysFont("bahnschrift",25)
		text = font_style.render("Score : " + str(score),True,(255,255,255))
		text1 = font_style.render("Level : " + str(level),True,(255,255,255))
		screen.blit(text,(0,0))
		screen.blit(text1,(400,0))
		pygame.display.update()

		
		if(x_food == x_snake and y_food == y_snake):
			eating_sound = mixer.Sound('eating.wav')
			eating_sound.play()
			score += 10
			count += 1
			x_food = random.randrange(25,475,25)#random food generation
			y_food = random.randrange(25,475,25)
			snake_length += 1
			if (count % 5) == 0:
				level += 1
				fps += 2
		x_center = x_food + 12.5
		y_center = y_food + 12.5
		food = pygame.draw.circle(screen,(255,0,0),(x_center,y_center),12.5)
		pygame.display.update()

		time.tick(fps)
	pygame.quit()
	quit()

while True:
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				game_loop()
