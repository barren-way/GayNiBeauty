import pygame
from pygame.sprite import Sprite
from ship import ship


class basketball():
    def __init__(self,ai_setting,screen,x,y,cai):
        
        self.ai_setting=ai_setting
        #self.direction_x=x
        #self.basketball_direction_y=y
        self.basketball_direction_y=y
        self.basketball_direction_x=x
        

        
        self.screen=screen
        self.image=pygame.image.load('image/basketball.png')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()

        self.rect.centerx=cai.rect.centerx
        self.rect.top=cai.rect.top+20
        self.y=float(self.rect.y)
        self.x=float(self.rect.x)

        self.color = ai_setting.bullet_color
        self.speed_factor = ai_setting.bullet_speed_factor

    def update(self):
        self.y+=self.ai_setting.basketball_speed*self.basketball_direction_y
        self.x+=self.ai_setting.basketball_speed*self.basketball_direction_x
        if self.rect.right>self.screen_rect.right:
            self.x-=20
            self.basketball_direction_x*=-1
        if  self.rect.top<self.screen_rect.top:
            self.y+=20
            self.basketball_direction_y*=-1
        elif self.rect.left<self.screen_rect.left:
            self.x+=20
            self.basketball_direction_x*=-1
        elif self.rect.bottom>self.screen_rect.bottom:
            self.y-=20
            self.basketball_direction_y*=-1
        self.rect.y=self.y
        self.rect.x=self.x

    def draw_basketball(self):
        self.screen.blit(self.image,self.rect)
        
