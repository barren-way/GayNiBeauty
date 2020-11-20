import pygame
from pygame.sprite import Sprite
from ship import ship

class Music():
    def __init__(self,ai_setting,screen,cai,stats,sb,gf):
        
        self.screen=screen
        self.ai_setting=ai_setting
        
        #加载飞船图像并获取外接矩形
        self.image=pygame.image.load('image/music.png')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()

        #将每艘新飞船放在屏幕底部中央
        self.rect.centerx=self.screen_rect.centerx
        self.rect.top=self.screen_rect.top
        
        self.center=float(self.rect.centerx)
        self.top=float(self.rect.top)

        self.rect.x=self.rect.width
        self.rect.y = self.rect.top
        self.x=float(self.rect.x)
        
        

    def update(self,cai,ship,ai_setting,stats,sb,gf):
        self.rect.x=cai.rect.x-170
        self.rect.y=cai.rect.y-190
        if pygame.Rect.colliderect(self.rect,ship.rect):
            if stats.ship_left>0:
                stats.ship_left-=ai_setting.cai_music
                sb.prep_life()
            else:
                gf.ni_die(stats,sb,ai_setting)

        

    def blitme(self):
        self.screen.blit(self.image,self.rect)


    
