import pygame
import os 
import random
# first time coidng in python :monka:
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
hearts = pygame.image.load(os.path.join('Artwork/Heart.png'))
current = pygame.image.load(os.path.join('Artwork/DRAW CARD ANIMATION.png'))
draw = []
heartCount = 3
blankCard = pygame.image.load(os.path.join('Artwork/DRAW CARD ANIMATION.PNG'))
class Button(object):
    def __init__(self, position, filename):
        self.image = pygame.image.load(os.path.join(f'Artwork/{filename}'))
        self.rect = self.image.get_rect(topleft=position)
    def draw(self,surface):
        surface.blit(self.image,self.rect)
    def check_press(self,position):
        if(self.rect.collidepoint(*position)):
            return True
        return False
nextButton = Button((1180,670), "Drawcard.png")
endButton = Button((0,670), "Endround.png")
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if nextButton.check_press(event.pos):
                rnd = random.randint(1,25)
                current = pygame.image.load(os.path.join(f'Artwork/card{rnd}.png')) 
            #if(nextButton.check_press(event.pos)):
            
    screen.blit(blankCard, (950, 200))            
    nextButton.draw(screen)
    endButton.draw(screen)
    screen.blit(current, (450,375))
    if(heartCount == 3):
        screen.blit(hearts, (0, 0))
        screen.blit(hearts, (50, 0))
        screen.blit(hearts, (100, 0))
    elif(heartCount == 2):
        screen.blit(hearts, (0, 0))
        screen.blit(hearts, (50, 0))
    elif(heartCount == 1):
        screen.blit(hearts, (0, 0))
    #else:
        #add round end
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()