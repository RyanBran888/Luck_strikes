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
gold = 0
totalGold = 0
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
                if(rnd == 1):
                    heartCount = 0
                elif(rnd == 2):
                    gold += 5
                elif(rnd == 3):
                    gold += 10
                elif(rnd == 4):
                    # peak
                    rnd = 5
                elif(rnd == 5):
                    heartCount -= 1
                elif(rnd == 6):
                    heartCount += 1
                elif(rnd == 7):
                    gold = gold * 2
                elif(rnd == 8):
                    heartCount -= 1
                    if(gold % 2 == 0):
                       gold = gold/2
                    else:
                        gold = gold/2
                        difference = 1 - gold
                        gold += (difference*-1)
                elif(rnd == 9):
                    rnd = 10
                    #shuffle
                elif(rnd == 10):
                    gold += 1
                elif(rnd == 11):
                    gold = gold * 2
                elif(rnd == 12):
                    gold = gold *0
                elif(rnd == 13):
                    #multiuple choice
                    rnd = 14
                elif(rnd == 14):
                    #ahgain more choice
                    rnd = 15
                elif(rnd == 15):
                    heartCount+= 2
                elif(rnd == 16):
                    gold+= 15
                elif(rnd == 17):
                    gold+= 10
                elif(rnd == 18):
                    gold+= 10
                elif(rnd == 19):
                    gold+= 9
                elif(rnd == 20):
                    gold+= 8
                elif(rnd == 21):
                    gold+= 7
                elif(rnd == 22):
                    gold+= 6
                elif(rnd == 23):
                    gold+= 5
                elif(rnd == 24):
                    gold+= 4
                elif(rnd == 25):
                    gold+= 3
            #if(endButton.check_press(event.pos)):
            
    screen.blit(blankCard, (950, 200))            
    nextButton.draw(screen)
    endButton.draw(screen)
    screen.blit(current, (450,375))
    if(heartCount == 5):
        screen.blit(hearts, (0, 0))
        screen.blit(hearts, (50, 0))
        screen.blit(hearts, (100, 0))
        screen.blit(hearts, (150, 0))
        screen.blit(hearts, (200, 0))
    elif(heartCount == 4):
        screen.blit(hearts, (0, 0))
        screen.blit(hearts, (50, 0))
        screen.blit(hearts, (100, 0))
        screen.blit(hearts, (150, 0))
    elif(heartCount == 3):
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