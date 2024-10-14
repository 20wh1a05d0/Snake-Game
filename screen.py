import pygame
pygame.init()
screen = pygame.display.set_mode((500,500),flags = 0,depth = 0)
pygame.display.set_caption("snake game!")
pygame.display.update()
y = 25
for i in range(19):
    pygame.draw.line(screen,(255,255,255),(0,y),(500,y))
    y += 25
x = 25
for i in range(19):
    pygame.draw.line(screen,(255,255,255),(x,0),(x,500))
    x += 25
    
pygame.display.update()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #for closing the window
            run = False
    
            
pygame.quit()
