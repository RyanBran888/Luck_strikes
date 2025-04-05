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
heartCount = 3

class Button(object):
    def init(self, position, filename):
        self.image = pygame.image.load(os.path.join(f'Artwork/{filename}'))
        self.rect = self.image.get_rect(topleft=position)
    def draw(self,surface):
        surface.draw(self.image,self.rect)
    def check_press(self,position):
        if(self.rect.collidepoint(*position)):
            return True
        return False
nextButton = Button((100,100), "Drawcard.png")
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN: 
                rnd = random.randint(1,25)
                current = pygame.image.load(os.path.join(f'Artwork/card{rnd}.png')) 
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if nextButton.check_press(event.pos):
                print("meow meow")
                
    nextButton.draw(screen)
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