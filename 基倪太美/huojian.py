import pygame
from pygame.sprite import Sprite

class Huojian(Sprite):
    def __init__(self,ai_setting,screen):
        super(Huojian,self).__init__()
        self.screen=screen
        self.ai_setting=ai_setting
        
        #加载火箭图像，并设置其rect属性
        self.image = pygame.image.load('image/hj.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.width = self.rect.width

        #每个火箭最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height-550

        #存储火箭的准确位置
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
    def blitme(self):
        """在指定位置绘制外星人"""
        self.screen.blit(self.image,self.rect)

    def update(self):
        self.y += self.ai_setting.huojian_speed_factor
        self.rect.y = self.y


