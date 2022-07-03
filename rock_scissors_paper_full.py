import pygame
import random
from time import sleep

WIDTH = 300
HEIGHT = 300
BACKGROUND = (255, 255, 255)

class Match:

    def __init__(self):
        picture = pygame.image.load("dinosaur.gif")
        self.image = pygame.transform.scale(picture, (100, 100))
        self.imageRect = self.image.get_rect(center=(WIDTH // 2 , HEIGHT // 2  ))
        self.choice = "dinosaur"
        self.state = ""
        self.count = 0
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.text = self.font.render('', True, (0,0,0), (255,255,255))   
        self.textRect = self.text.get_rect(center=(WIDTH // 2 - 50, HEIGHT // 2 - 100))

        self.playerOneScore = 0
        self.playerOneText = self.font.render(str(self.playerOneScore), True, (0,0,0), (255,255,255))   
        self.playerOneRect = self.playerOneText.get_rect(center=(50, HEIGHT - 20))

        self.playerTwoScore = 0
        self.playerTwoText = self.font.render(str(self.playerTwoScore), True, (0,0,0), (255,255,255))   
        self.playerTwoRect = self.playerTwoText.get_rect(center=(WIDTH - 50, HEIGHT - 20))

    def playerOne(self):
        self.playerOneText = self.font.render(str(self.playerOneScore), True, (0,0,0), (255,255,255))   
        self.playerOneRect = self.playerOneText.get_rect(center=(50, HEIGHT - 20))

    def playerTwo(self):
        self.playerTwoText = self.font.render(str(self.playerTwoScore), True, (0,0,0), (255,255,255))   
        self.playerTwoRect = self.playerTwoText.get_rect(center=(WIDTH - 50, HEIGHT - 20))

    def refresh(self):
        if self.count > 0: 
            self.count -= 1
        elif self.count <= 10:
            self.choice = "dinosaur"
            self.state = ""
        picture = pygame.image.load(f"{self.choice}.png")
        self.image = pygame.transform.scale(picture, (100, 100))
        self.text = self.font.render(self.state, True, (0,0,0), (255, 255, 255))   
        self.textRect = self.text.get_rect(center=(WIDTH/2, HEIGHT/2-100))

    def update(self, c):
        if self.count == 0:
            self.choice = c
            self.count = 100
            self.checkLogic(c)

    def checkLogic(self, c):
        d = {
            'rock': 1,
            'scissors': 2,
            'paper': 3
        }
        P1 = d[c]
        P2 = random.randint(1,3)
        if P1 == P2:
            self.state = "Draw"
        elif P1 == 1 and P2 == 2 or P1 == 2 and P2 == 3 or P1 == 3 and P2 == 1:
            self.state = "Com Win!"
            self.playerTwoScore += 1
        elif P2 == 1 and P1 == 2 or P2 == 2 and P1 == 3 or P2 == 3 and P1 == 1:
            self.state = "P1 Win!"
            self.playerOneScore += 1
        
        self.playerOne()
        self.playerTwo()

def main():
    clock = pygame.time.Clock()
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    match = Match()
    
    while True:
        pygame.event.get()

        if pygame.key.get_pressed()[pygame.K_z]:
            match.update('rock')
        
        elif pygame.key.get_pressed()[pygame.K_x]:
            match.update('scissors')

        elif pygame.key.get_pressed()[pygame.K_c]:
            match.update('paper')

        elif pygame.key.get_pressed()[pygame.K_q]:
            break
        
        screen.fill(BACKGROUND)
        screen.blit(match.image, match.imageRect)
        screen.blit(match.text, match.textRect)
        screen.blit(match.playerOneText, match.playerOneRect)
        screen.blit(match.playerTwoText, match.playerTwoRect)
        match.refresh()
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()