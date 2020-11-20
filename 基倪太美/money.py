import pygame
from pygame.sprite import Sprite
from niao import niao


class Money(Sprite):
    def __init__(self,ai_setting,screen,niao):
        super(Money,self).__init__()
        self.screen=screen
        self.ai_setting=ai_setting
        self.image=pygame.image.load('image/money.png').convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.centerx=niao.rect.centerx
        self.rect.bottom=niao.rect.bottom

        
        self.y=float(self.rect.y)
        self.x=float(self.rect.x)
        
        self.speed_factor = ai_setting.money_speed_factor
        self.fleet_drop_speed = ai_setting.fleet_drop_speed_money
    def update(self,a,b):
        for a in range(3):
            b = pow((9-pow(a,2)),0.5)
        self.y+=(self.fleet_drop_speed*a)
        self.x+=(self.speed_factor*b)
        self.rect.y=self.y
        self.rect.x=self.x
    
       

    def check_edges(self):
        screen_rect=self.screen.get_rect()
        if self.rect.right>=screen_rect.right:
            return True
        if self.rect.left<=0:
            return True
    def check_edges(self):
        """如果火箭位于屏幕边缘，就返回True"""
        screen_rect = self.screen.get_rect()
        if self.rect.top>=screen_rect.bottom:
            return True

