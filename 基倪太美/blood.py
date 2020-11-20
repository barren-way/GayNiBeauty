import pygame
from pygame.sprite import Sprite

class blood():
    def __init__(self,ai_setting,screen,max_blood,stats):
        self.screen=screen
        self.blood_width=1500/max_blood*ai_setting.cai_life
        self.blood_height=10
        self.rect = pygame.Rect(0,0,self.blood_width,self.blood_height)
        self.rect.left=200
        self.rect.top=50
        self.y=float(self.rect.y)
        self.x=float(self.rect.x)

        self.color =(255,0,0)
        self.color_white=(255,255,250)
        self.max_blood=max_blood
        self.blood_width_white=1350
        self.life=ai_setting.cai_life
        

    def draw_blood(self,ai_setting,stats):
        #self.screen.blit(self.image,self.rect)
        if stats.level==2:
            self.life=ai_setting.cai_life
        if stats.level==4:
            self.life=ai_setting.niao_life
        if stats.level==6:
            self.life=stats.xiong_left
        if stats.level==8:
            self.life=ai_setting.diao_life
        self.blood_width=1350 /self.max_blood*self.life

        self.rect_white = pygame.Rect(0,0,self.blood_width_white,self.blood_height)
        pygame.draw.rect(self.screen,self.color_white,self.rect_white)
        self.rect = pygame.Rect(0,0,self.blood_width,self.blood_height)
        pygame.draw.rect(self.screen,self.color,self.rect)
