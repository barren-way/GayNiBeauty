import pygame
from pygame.sprite import Sprite
from xiong import xiong


class Qzg(Sprite):
    def __init__(self,ai_setting,screen,xiong):
        super(Qzg,self).__init__()
        self.screen=screen
        self.ai_setting=ai_setting
        self.image=pygame.image.load('image/2.png').convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.centerx=xiong.rect.centerx
        self.rect.top=xiong.rect.bottom

        
        
        self.x=float(self.rect.x)
        
        self.speed_factor = ai_setting.qzg_speed_factor/2
         
    def update(self):
        
        self.x+=self.speed_factor*self.ai_setting.fleet_direction_qzg
        
        self.rect.x=self.x
    
       

    def check_edges(self):
        screen_rect=self.screen.get_rect()
        if self.rect.right>=screen_rect.right:
            return True
        if self.rect.left<=0:
            return True
