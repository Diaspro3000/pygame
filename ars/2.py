import pygame
import random

RES = (400, 600)

screen = pygame.display.set_mode(RES)
clock = pygame.time.Clock()
FPS = 60

WHITE = (255, 255, 255)
RED = (255, 0, 0)
transparent = (0, 0, 0, 0)
        


class Car(pygame.sprite.Sprite,):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.image.load("Player.jpg")
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.y = 0
        self.speed = 12
        self.score = 0

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        elif keys[pygame.K_d]:
            self.rect.x += self.speed
        elif keys[pygame.K_s]:
            self.rect.y += self.speed
        elif keys[pygame.K_w]:
            self.rect.y -= self.speed
        
            
            


    def draw(self):
        screen.blit(self.image, self.rect)





class enemy_car(pygame.sprite.Sprite):
    def __init__(self,):
        super().__init__()
        self.image = pygame.image.load("Enemy.jpg")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(50, 300), 0)
        self.death = pygame.image.load("you_died.png")
        self.death = pygame.transform.scale(self.death, (200, 100))
        self.speed = 10
        

    def update(self):
        self.rect.y += self.speed
        if  self.rect.y > 700:
            self.rect.y = -100
            self.rect.center = (random.randint(50, 300), -100)

    def kill(self, Car):
        if Car.rect.colliderect(self.rect):
            screen.blit(self.death, (100, 100))
            self.rect.y -= self.speed
        
        
        

    def draw(self):
        screen.blit(self.image, self.rect)
        if self.rect.x < 0:
            self.kill


class coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Coin.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(50, 300), random.randint(50, 300))
        self.speed = 10

    def draw(self):
        screen.blit(self.image, self.rect)
        

    def update(self, Car):
        self.rect.y += self.speed
        if  self.rect.y > 700:
            self.rect.y = -100
            self.rect.center = (random.randint(50, 300), -100)
        if Car.rect.colliderect(self.rect):
            self.kill()
            

      



running = True
d = Car((100, 500))
c = enemy_car()
cn = coin()


pygame.init() 


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

    screen.fill(WHITE)
    d.update()
    c.update()
    cn.update(d)
    
    d.draw()
    c.draw()
    cn.draw()
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

