from typing import Any
import pygame
import random


 

FPS = 60
clock = pygame.time.Clock()
WHITE = (255, 255, 255)
screen = pygame.display.set_mode((400, 600))



class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Enemy.jpg')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, 400), 0)
        self.speed = random.randint(5,10)

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 600:
            self.rect.center = (random.randint(0, 400), 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Player.jpg')
        self.rect = self.image.get_rect()
        self.rect.center = (200, 500)

    def update(self):
        key = pygame.key.get_pressed()
        if self.rect.x > 0:
            if key[pygame.K_LEFT]:
                self.rect.x -= 10
        if self.rect.x < 350:
            if key[pygame.K_RIGHT]:
                self.rect.x += 10

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(50, 300), random.randint(50, 300))

    def draw(self):
        screen.blit(self.image, self.rect)

    

running = True
E = Enemy()
P = Player()
all = pygame.sprite.Group()
all.add(E)
all.add(P)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(WHITE)
    all.draw(screen)
    all.update()
    if E.rect.colliderect(P.rect):
        running = False
    pygame.display.flip()
    clock.tick(FPS)

