import pygame
import os 
# first time coidng in python :monka:
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
current = pygame.image.load(os.path.join('Artwork/Card1.png'))
draw = []
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN: 
                draw.append(current)
             
    for img in draw:
        screen.blit(img, (100,100))
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()