import pygame
import os
import random

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.running = True

        # Game variables
        self.hearts = pygame.image.load(os.path.join('Artwork/Heart.png'))
        self.blankCard = pygame.image.load(os.path.join('Artwork/DRAW CARD ANIMATION.PNG'))
        self.current = self.blankCard
        self.draws = []
        self.gold = 0
        self.heartCount = 3
        self.runOne = False

        # Buttons
        self.nextButton = self.Button((1180, 670), "Drawcard.png")
        self.endButton = self.Button((0, 670), "Endround.png")
        self.leftButton = self.Button((1180, 500), "leftButton.png")
        self.rightButton = self.Button((0, 500), "buttonright.png")

    class Button:
        def __init__(self, position, filename):
            self.image = pygame.image.load(os.path.join(f'Artwork/{filename}'))
            self.rect = self.image.get_rect(topleft=position)

        def draw(self, surface):
            surface.blit(self.image, self.rect)

        def check_press(self, position):
            return self.rect.collidepoint(*position)

    def draw_hearts(self):
        for i in range(self.heartCount):
            self.screen.blit(self.hearts, (i * 50, 0))

    def handle_card_effect(self, rnd):
        if rnd == 1:
            self.heartCount = 0
        elif rnd == 2:
            self.gold += 5
        elif rnd == 3:
            self.gold += 10
        elif rnd == 4:
            for i, pos in enumerate([(100, 100), (450, 25), (800, 100)]):
                self.screen.blit(pygame.image.load(os.path.join(f'Artwork/card{self.draws[i + 1]}.png')), pos)
        elif rnd == 5 or rnd == 8:
            self.heartCount -= 1
            if rnd == 8:
                self.gold = self.gold // 2
        elif rnd == 6:
            self.heartCount += 1
        elif rnd == 7 or rnd == 11:
            self.gold *= 2
        elif rnd == 9:
            self.draws.clear()
        elif rnd == 10:
            self.gold += 1
        elif rnd == 12:
            self.gold = 0
        elif rnd == 13 or rnd == 14:
            self.leftButton.draw(self.screen)
            self.rightButton.draw(self.screen)
        elif rnd == 15:
            self.heartCount += 2
        elif rnd in range(16, 26):
            self.gold += rnd - 15

    def run(self):
        while self.running:
            if len(self.draws) < 5:
                self.draws.extend(random.randint(1, 25) for _ in range(5 - len(self.draws)))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.nextButton.check_press(event.pos):
                        if self.runOne and self.draws[0] in [4, 5, 8]:
                            self.screen.fill((0, 0, 0))
                            self.screen.blit(self.blankCard, (950, 200))
                        rnd = self.draws.pop(0)
                        self.runOne = True
                        self.current = pygame.image.load(os.path.join(f'Artwork/card{rnd}.png'))
                        self.handle_card_effect(rnd)
                    elif self.leftButton.check_press(event.pos):
                        self.heartCount += 1
                        self.screen.fill((0, 0, 0))
                        self.screen.blit(self.blankCard, (950, 200))
                    elif self.rightButton.check_press(event.pos):
                        self.gold += 5 if rnd == 13 else 1
                        self.screen.fill((0, 0, 0))
                        self.screen.blit(self.blankCard, (950, 200))

            self.screen.fill((0, 0, 0))
            self.screen.blit(self.blankCard, (950, 200))
            self.nextButton.draw(self.screen)
            self.endButton.draw(self.screen)
            self.screen.blit(self.current, (450, 375))
            self.draw_hearts()
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

# Run the game
if __name__ == "__main__":
    game = Game()
    game.run()