import pygame
from setting import setting
from pygame.sprite import Sprite

class xiong():
    def __init__(self,ai_setting,screen):
        self.screen=screen
        self.ai_setting=ai_setting
        
        #加载xjc图像并获取外接矩形
        self.image=pygame.image.load('image/xiong.png').convert_alpha() 
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()

        #将xjc放在屏幕顶部中央
        self.rect.centerx=self.screen_rect.centerx
        self.rect.top=self.screen_rect.top
        
        self.centerx=float(self.rect.centerx)
        self.top=float(self.rect.top)
        self.bottom=float(self.rect.bottom)
        self.rect.x=self.rect.width
        self.rect.y = self.rect.height
        self.x=float(self.rect.x)
        self.y=float(self.rect.y)
        self.rect.centerx=self.centerx
        self.rect.top=self.top



    def update(self):
        self.x+=self.ai_setting.xiong_speed_factor*self.ai_setting.fleet_direction_cong
        self.rect.x=self.x



        

    def blitme(self):
        self.screen.blit(self.image,self.rect)
        self.rect.centerx=self.centerx


    #将飞船放置在屏幕底端
    def center_niao(self):
        self.center=self.screen_rect.centerx
        self.top=self.screen_rect.top
    
    def check_edges(self):
        screen_rect=self.screen.get_rect()
        if self.rect.right>=screen_rect.right:
            return True
        if self.rect.left<=0:
            return True
