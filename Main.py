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
draws = []
gold = 0
totalGold = 0
heartCount = 3
shop = False
q = 0
runOne = False
Buttons = False
font = pygame.font.SysFont("Arial", 30)
Tcolor = (255, 255, 255)
blankCard = pygame.image.load(os.path.join('Artwork/DRAW CARD ANIMATION.PNG'))
screen.blit(blankCard, (950, 200))   
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
leftButton = Button((1180,500), "leftButton.png")
rightButton = Button((0,500), "buttonright.png")
alphabet = pygame.image.load(os.path.join('Artwork/pack1'))
while running: 
    if(shop == False):
    
        if(draws.__len__() != 5):
                        for i in range(draws.__len__(), 5):
                            draws.append(random.randint(1,25))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if nextButton.check_press(event.pos):
                    if(runOne):
                        screen.fill((0,0,0))
                        screen.blit(blankCard, (950, 200))
                    print(draws)
                    draws.pop(0)
                    rnd = draws[0]
                    runOne = True
                    current = pygame.image.load(os.path.join(f'Artwork/card{rnd}.png'))
                    if(rnd == 1):
                        heartCount = 0
                    elif(rnd == 2):
                        gold += 5
                    elif(rnd == 3):
                        gold += 10
                    elif(rnd == 4):
                        screen.blit(pygame.image.load(os.path.join(f'Artwork/card{draws[1]}.png')), (100, 100))
                        screen.blit(pygame.image.load(os.path.join(f'Artwork/card{draws[2]}.png')), (450, 25))
                        screen.blit(pygame.image.load(os.path.join(f'Artwork/card{draws[3]}.png')), (800, 100))
                    elif(rnd == 5):
                        heartCount = heartCount - 1
                    elif(rnd == 6):
                        heartCount += 1
                    elif(rnd == 7):
                        gold = gold * 2
                    elif(rnd == 8):
                        heartCount = heartCount - 1
                        if(gold % 2 == 0):
                           gold = gold/2
                        else:
                            gold = gold/2
                            difference = 1 - gold
                            gold += (difference*-1)
                    elif(rnd == 9):
                        #fix
                        for i in draws:
                            draws.pop(0)
                    elif(rnd == 10):
                        gold += 1
                    elif(rnd == 11):
                        gold = gold * 2
                    elif(rnd == 12):
                        gold = gold *0
                    elif(rnd == 13):
                        Buttons = True 
                    elif(rnd == 14):
                        Buttons = True
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
                if(endButton.check_press(event.pos)):
                    totalGold += gold
                    gold = 0
                    shop = True
                if(Buttons):
                    print("meow")
                    leftButton.draw(screen)
                    rightButton.draw(screen)
                    if(leftButton.check_press(event.pos)):
                        heartCount += 1
                        screen.fill((0,0,0))
                        screen.blit(blankCard, (950, 200))
                        Buttons = False
                    elif(rightButton.check_press(event.pos)):
                        if(rnd == 13):
                            gold += 5
                        else:
                            gold+= 1
                        screen.fill((0,0,0))
                        screen.blit(blankCard, (950, 200))
                        Buttons = False         
        nextButton.draw(screen)
        endButton.draw(screen)
        screen.blit(current, (450,375))
        textsend = font.render(f"Coins: {gold}", True, Tcolor)
        screen.blit(textsend, (500, 0))
        if(heartCount == 8):
            screen.blit(hearts, (0, 0))
            screen.blit(hearts, (50, 0))
            screen.blit(hearts, (100, 0))
            screen.blit(hearts, (150, 0))
            screen.blit(hearts, (200, 0)) 
            screen.blit(hearts, (250, 0))
            screen.blit(hearts, (300, 0))
            screen.blit(hearts, (350, 0))
        elif(heartCount == 7):
            screen.blit(hearts, (0, 0))
            screen.blit(hearts, (50, 0))
            screen.blit(hearts, (100, 0))
            screen.blit(hearts, (150, 0))
            screen.blit(hearts, (200, 0)) 
            screen.blit(hearts, (250, 0))
            screen.blit(hearts, (300, 0))
        elif(heartCount == 6):
            screen.blit(hearts, (0, 0))
            screen.blit(hearts, (50, 0))
            screen.blit(hearts, (100, 0))
            screen.blit(hearts, (150, 0))
            screen.blit(hearts, (200, 0)) 
            screen.blit(hearts, (250, 0)) 
        elif(heartCount == 5):
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
            # print(draws)
            screen.blit(hearts, (0, 0))
            screen.blit(hearts, (50, 0))
            screen.blit(hearts, (100, 0))
        elif(heartCount == 2):
            screen.blit(hearts, (0, 0))
            screen.blit(hearts, (50, 0))
        elif(heartCount == 1):
            screen.blit(hearts, (0, 0))
        elif(heartCount == 0):
            gold = 0
            shop = True
        pygame.display.flip()
        clock.tick(60)
    elif(shop):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and totalGold >= 5:
                q += 1
                if(q == 1):
                    alphabet = pygame.image.load(os.path.join('Artwork/pack3'))
                else:
                    alphabet = random.randrange(1, 10)
        screen.blit(alphabet, (300, 375))            
        pygame.display.flip()
        clock.tick(60)
pygame.quit()