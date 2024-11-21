import pygame
import random
pygame.init()

screen = pygame.display.set_mode((1210,690))

bg = pygame.image.load("lesson 8/images/bg.png")
bin = pygame.image.load("lesson 8/images/bin.png")
bin = pygame.transform.scale(bin,(50,89))
box = pygame.image.load("lesson 8/images/box.png")
paper_bag = pygame.image.load("lesson 8/images/paper bag.png")
pencil = pygame.image.load("lesson 8/images/pencil.png")
plastic_bag = pygame.image.load("lesson 8/images/plastic bag.png")

images = [box,paper_bag,pencil]

class Bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = bin
        self.rect = self.image.get_rect()

class Recycle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = random.choice(images)
        self.rect = self.image.get_rect()

class Plastic_bag(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = plastic_bag
        self.rect = self.image.get_rect()

binn = pygame.sprite.Group()
recycle = pygame.sprite.Group()
plastic = pygame.sprite.Group()

Binn = Bin()
binn.add(Binn)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                Binn.rect.y -= 2
        
    screen.fill("black")
    screen.blit(bg,(0,0))
    binn.draw(screen)
    pygame.display.update()