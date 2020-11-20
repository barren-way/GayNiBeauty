import pygame
from pygame.sprite import Sprite
from ship import ship


class Abuse(Sprite):
    def __init__(self,ai_setting,screen,ship,x,y,stats,diao,image):
        super(Abuse,self).__init__()
        self.screen=screen
        self.image =pygame.image.load(image)
            
        self.rect =self.image.get_rect()
        self.screen_rect=screen.get_rect()
       
        self.rect.centerx=diao.rect.centerx
        self.rect.top=diao.rect.top
        self.y=float(self.rect.y)
        self.x=float(self.rect.x)

        
        self.speed_factor = 4

        self.direction_x=x
        self.direction_y=y
    def update(self):
        self.y+=self.speed_factor*self.direction_y
        self.x+=self.speed_factor*self.direction_x
        self.rect.y=self.y
        self.rect.x=self.x
        

    def draw_abuse(self):
     
        self.screen.blit(self.image,self.rect)
       