import pygame
from pygame.sprite import Sprite
from ship import ship

class Cai():
    def __init__(self,ai_setting,screen):
        
        self.screen=screen
        self.ai_setting=ai_setting
        
        #加载飞船图像并获取外接矩形
        self.image=pygame.image.load('image/cai.png')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()

        #将每艘新飞船放在屏幕底部中央
        self.rect.centerx=self.screen_rect.centerx
        self.rect.top=self.screen_rect.top
        
        self.center=float(self.rect.centerx)
        self.top=float(self.rect.top)

        self.rect.x=self.rect.width
        self.rect.y = self.rect.top+10
        self.x=float(self.rect.x)
        self.y=float(self.rect.y)
        
        

    def update(self):
        if self.check_edges():
            self.ai_setting.cai_direction*=-1

        self.x+=self.ai_setting.cai_speed*self.ai_setting.cai_direction
        self.rect.x=self.x

        

    def blitme(self):
        self.screen.blit(self.image,self.rect)


    #将飞船放置在屏幕底端
    def center_cai(self):
        self.center=self.screen_rect.centerx
        self.top=self.screen_rect.top

    def check_edges(self):
        screen_rect=self.screen.get_rect()
        if self.rect.right>=screen_rect.right:
            return True
        if self.rect.left<=0:
            return True
#蔡位移到篮球处
    def jump_cai(self,basketball):
        self.rect.x=basketball.x+10
        self.rect.y=basketball.y-20





    