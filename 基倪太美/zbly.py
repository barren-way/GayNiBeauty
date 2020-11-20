import pygame
from pygame.sprite import Sprite
from xiong import xiong
class Zbly():
    def __init__(self,ai_setting,screen,xiong):
        self.screen=screen
        self.ai_setting=ai_setting
        
        #加载外星人，设置rect
        self.image=pygame.image.load('image/shsm.png').convert_alpha()
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()

        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
        self.x = self.rect.x
        self.y = self.rect.y
    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def update(self):
        self.x+=self.ai_setting.zbly_speed_factor*self.ai_setting.fleet_direction
        self.y+=self.ai_setting.zbly_speed_factor*self.ai_setting.fleet_direction
        self.rect.x=self.x
        self.rect.y = self.y
    def check_edges(self):
        screen_rect=self.screen.get_rect()
        if self.rect.right>=screen_rect.right:
            return True
        if self.rect.left<=0:
            return True
