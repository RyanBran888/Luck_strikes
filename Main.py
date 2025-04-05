import pygame
import os 
import random
# first time coidng in python :monka:
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
hearts = pygame.image.load(os.path.join('Artwork/Heart.png'))
current = pygame.image.load(os.path.join('Artwork/card1.png'))
draw = []
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN: 
                draw.append(current)
             
    for img in draw:
        screen.blit(img, (450,375))
    screen.blit(hearts, (0, 0))
    screen.blit(hearts, (50, 0))
    screen.blit(hearts, (100, 0))
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()