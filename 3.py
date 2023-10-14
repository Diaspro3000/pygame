from typing import Any
import pygame, random


image_lazer = pygame.image.load('PythonPygame-main/sprites/laser.png')
image_rock = pygame.image.load('PythonPygame-main\sprites\stone.png')
sizes = [[64, 64], [96, 96], [128, 128], [160, 160], [198, 198]]
rocks = []
for size in sizes:
    rocks.append(pygame.transform.scale(image_rock, size))
RES = (800, 600)

ekran = pygame.display.set_mode(RES)
clock = pygame.time.Clock()
FPS = 60

running = True
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

class Player(pygame.sprite.Sprite,):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('PythonPygame-main\sprites\spaceship.png')
        self.rect = self.image.get_rect()
        self.rect.center = (400, 400)
        self.speed = 15
        self.shoot_delay = 100
        self.last_shoot = pygame.time.get_ticks()
        

    def update(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
           
        elif keys[pygame.K_s]:
            self.rect.y += self.speed
          
        elif keys[pygame.K_a]:
            self.rect.x -= self.speed
         
        elif keys[pygame.K_d]:
            self.rect.x += self.speed
        self.shoot()
        

    def shoot(self):
        now = pygame.time.get_ticks()
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_SPACE]:
            if now - self.last_shoot - self.shoot_delay > 0:
                coords = self.rect.center
                ans = [(coords[0] + 17, coords[1] - 25), (coords[0] - 17, coords[1] - 25), (coords[0] + 27, coords[1] - 5), (coords[0] - 27, coords[1] -5)]
                bullet = Bullet((random.choice(ans)))
                all_sprites.add(bullet)
                bullets.add(bullet)
                self.last_shoot = now
                
class Rock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.index = random.randint(0, 4)
        self.image = rocks[self.index]
        self.radius = sizes[self.index][0] // 2
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(800 - self.rect.width)
        self.rect.y = random.randrange(-150, -100)
        self.rot_speed = random.randrange(-4, 4)
        self.rot_angle = 0
        self.dx = random.uniform(-7, 7)
        self.dy = random.uniform(1, 7)
        self.last_update = pygame.time.get_ticks()


    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            new_image = pygame.transform.rotate(rocks[self.index], self.rot_angle)
            self.rot_angle = (self.rot_angle + self.rot_speed) % 360
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center

    def update(self):
        coords = self.rect.center
        #enemy bounces off the borders
        if(coords[0] + self.dx <- 128):
            self.kill()
        elif(coords[0] + self.dx > 928):
            self.kill()
        else:
            coords = coords[0] + self.dx, coords[1]
        if(coords[1] + self.dy <- 128):
            self.kill()
        elif(coords[1] + self.dy > 728):
            self.kill()
        else:
            coords = coords[0], coords[1] + self.dy
        self.rect.center = coords
        self.rotate()

class Bullet (pygame.sprite.Sprite):
    def __init__(self, coords):
        super().__init__()
        self.image = image_lazer
        self.rect = self.image.get_rect()
        self.rect.center = coords
        self.dx = 0
        self.dy = -15

    def update(self):
        coords = self.rect.center
        if(coords[1] + self.dy < 50):
            self.kill()
        elif(coords[1] + self.dy > 550):
            self.kill()
        else:
            coords = coords[0], coords[1] + self.dy
        self.rect.center = coords
        



        
r = Rock()
p = Player()
all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
player = pygame.sprite.Group()
bullets = pygame.sprite.Group()
all_sprites.add(p, r)


def spawn():
    for i in range(10 - len(mobs)):
        t = Rock()
        all_sprites.add(t)
        mobs.add(t)
spawn()






pygame.init()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    spawn()
    hit_player = pygame.sprite.spritecollide(p, mobs, False, pygame.sprite.collide_circle)
    if hit_player:
        running = False

    ekran.fill((0,0,0 ))
    all_sprites.draw(ekran)
    all_sprites.update()
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()