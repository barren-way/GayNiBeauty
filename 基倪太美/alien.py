import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,ai_setting,screen,stats):
        super(Alien,self).__init__()
        self.screen=screen
        self.ai_setting=ai_setting
        self.image=pygame.image.load('image/alien.png')
        #加载外星人，设置rect
        if stats.level<3:
            self.image=pygame.image.load('image/alien.png')
        if stats.level>=3 and stats.level<5:
            self.image=pygame.image.load('image/money.png')
        if stats.level>=5 and stats.level<7:
            self.image=pygame.image.load('image/茄子干.png')
        if stats.level>=7 and stats.level<9:
            self.image=pygame.image.load('image/键盘.png')
        if stats.level>=9:
            self.image=pygame.image.load('image/胡雨杭.png')
        self.rect=self.image.get_rect()
        

        self.rect.x=self.rect.width
        self.rect.y = self.rect.height
        self.x=float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def update(self):
        self.x+=self.ai_setting.alien_speed_factor*self.ai_setting.fleet_direction/2
        self.rect.x=self.x

    def check_edges(self):
        screen_rect=self.screen.get_rect()
        if self.rect.right>=screen_rect.right:
            return True
        if self.rect.left<=0:
            return True

       