import pygame
from setting import setting


class ship(object):
    def __init__(self,ai_setting,screen,stats):
        self.screen=screen
        self.ai_setting=ai_setting
        
        #加载飞船图像并获取外接矩形
      
        self.image=pygame.image.load('image/鸡巴倪.png')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()

        #将每艘新飞船放在屏幕底部中央
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
        
        self.center=float(self.rect.centerx)
        self.bottom=float(self.rect.bottom)


        self.moving_right=False
        self.moving_left=False
        self.moving_up=False
        self.moving_down=False

        self.number=1
    def update(self):

        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.center+=self.ai_setting.ship_speed_factor
        if self.moving_up and self.rect.top>self.screen_rect.top:
            self.bottom-=self.ai_setting.ship_speed_factor
        elif self.moving_left and self.rect.left>self.screen_rect.left:
            self.center-=self.ai_setting.ship_speed_factor
        elif self.moving_down and self.rect.bottom<self.screen_rect.bottom:
            self.bottom+=self.ai_setting.ship_speed_factor

        self.rect.centerx=self.center
        self.rect.bottom=self.bottom
        self.old_center=self.center
        self.old_bottom=self.bottom

    def blitme(self,stats):
        
        if stats.level==1 and self.number<2:
            
            self.image=pygame.image.load('image/鸡巴倪.png')
            self.rect=self.image.get_rect()
            self.rect.centerx=self.screen_rect.centerx
            self.rect.bottom=self.screen_rect.bottom
            self.center=float(self.rect.centerx)
            self.bottom=float(self.rect.bottom)
            
            self.number=2
        if stats.level==2 and self.number<3:
            self.image=pygame.image.load('image/弟弟倪.png')
            self.rect=self.image.get_rect()
           
            self.rect.centerx=self.old_center
            self.rect.bottom=self.old_bottom
            self.center=float(self.rect.centerx)
            self.bottom=float(self.rect.bottom)
            self.number=3
        if stats.level==3 and self.number<4:
            self.image=pygame.image.load('image/狗肉倪.png')
            self.rect=self.image.get_rect()
           
            self.rect.centerx=self.old_center
            self.rect.bottom=self.old_bottom
            self.center=float(self.rect.centerx)
            self.bottom=float(self.rect.bottom)
            self.number=4
        if stats.level==4 and self.number<5:
            self.image=pygame.image.load('image/臭臭倪.png')
            self.rect=self.image.get_rect()
           
            self.rect.centerx=self.old_center
            self.rect.bottom=self.old_bottom
            self.center=float(self.rect.centerx)
            self.bottom=float(self.rect.bottom)
            self.number=5
        if stats.level==5 and self.number<6:
            self.image=pygame.image.load('image/臭倪.png')
            self.rect=self.image.get_rect()
           
            self.rect.centerx=self.old_center
            self.rect.bottom=self.old_bottom
            self.center=float(self.rect.centerx)
            self.bottom=float(self.rect.bottom)
            self.number=6
        if stats.level==6 and self.number<7:
            self.image=pygame.image.load('image/倪.png')
            self.rect=self.image.get_rect()
           
            self.rect.centerx=self.old_center
            self.rect.bottom=self.old_bottom
            self.center=float(self.rect.centerx)
            self.bottom=float(self.rect.bottom)
            self.number=7
        if stats.level==7 and self.number<8:
            self.image=pygame.image.load('image/倪中原.png')
            self.rect=self.image.get_rect()
           
            self.rect.centerx=self.old_center
            self.rect.bottom=self.old_bottom
            self.center=float(self.rect.centerx)
            self.bottom=float(self.rect.bottom)
            self.number=8
        if stats.level==8 and self.number<9:
            self.image=pygame.image.load('image/大哥倪.png')
            self.rect=self.image.get_rect()
           
            self.rect.centerx=self.old_center
            self.rect.bottom=self.old_bottom
            self.center=float(self.rect.centerx)
            self.bottom=float(self.rect.bottom)
            self.number=9
        if stats.level==9 and self.number<10:
            self.image=pygame.image.load('image/倪爷.png')
            self.rect=self.image.get_rect()
           
            self.rect.centerx=self.old_center
            self.rect.bottom=self.old_bottom
            self.center=float(self.rect.centerx)
            self.bottom=float(self.rect.bottom)
            self.number=10
        self.screen.blit(self.image,self.rect)
        

    #将飞船放置在屏幕底端
    def center_ship(self):
        self.center=self.screen_rect.centerx
        self.bottom=self.screen_rect.bottom
        


