import pygame
from pygame import *
from random import randint

class Naves(pygame.sprite.Sprite):
    def __init__(self, img, pos_x, pos_y, rot, velo ):
        pygame.sprite.Sprite.__init__(self)
        self.vida = 100
        self.vida_maxima = 100
        self.velo = velo
        self.rotation = rot
        self.image = pygame.image.load(img).convert_alpha()
        self.image = pygame.transform.scale(self.image, (70,70))
        self.image = pygame.transform.rotate(self.image, -self.rotation)
        
        self.rect = self.image.get_rect()
        self.rect.centery = pos_y
        self.rect.centerx = pos_x
        
        self.mask = pygame.mask.from_surface(self.image)
        
        
    def update(self):
        self.rect.x -= self.velo
        if self.rect.x < 0:
            self.rect.x = 1400
            self.rect.y = randint(150, 500)
            self.velo = randint(4, 10)



class Player(pygame.sprite.Sprite):
    def __init__(self, img, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.som_disparo_missil = pygame.mixer.Sound('sounds/Missil.mp3')
        self.velo = 10
        self.image = pygame.image.load(img).convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.image = pygame.transform.rotate(self.image, -90)
        
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image) 
        self.rect.centery = pos_y
        self.rect.centerx = pos_x
        self.vida = True
        
    def update(self):
        if self.vida == True:
            tecla = pygame.key.get_pressed()
            if tecla[pygame.K_UP] and self.rect.y > 1:
                self.rect.y -=self.velo
                
            if tecla[pygame.K_DOWN] and self.rect.y < 550:
                self.rect.y +=self.velo
            
            if tecla[pygame.K_RIGHT] and self.rect.x < 1400:
                self.rect.x +=self.velo
    
            if tecla[pygame.K_LEFT] and self.rect.x > 1:
                self.rect.x -=self.velo
            
             
    def criar_missil(self):
        return Missil(self.rect.centerx, self.rect.centery)
                        
                    
    def som_disparo(self):
        self.som_disparo_missil.play()
        
        

    
class Missil(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.velo = 20
        self.image = pygame.image.load('imagens/missil_3.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (25,50))
        self.image = pygame.transform.rotate(self.image, -90)

        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.centery = y
        self.rect.centerx = x
        
    def update(self):
        self.rect.centerx  += self.velo 

        
 

