import pygame
from pygame.sprite import Sprite
from ship import ship


class Sputtering(Sprite):
    def __init__(self,ai_setting,screen,x,y,stats,abuse):
        super(Sputtering,self).__init__()
        self.screen=screen
        self.rect = pygame.Rect(0,0,ai_setting.sputtering_width,ai_setting.sputtering_height)
            
        self.screen_rect=screen.get_rect()
        self.color = ai_setting.bullet_color
        self.rect.centerx=abuse.rect.centerx
        self.rect.top=abuse.rect.top
        self.y=float(self.rect.y)
        self.x=float(self.rect.x)

        
        self.speed_factor = 5
        self.direction_x=x
        self.direction_y=y
    def update(self):
        self.y+=self.speed_factor*self.direction_y
        self.x+=self.speed_factor*self.direction_x
        self.rect.y=self.y
        self.rect.x=self.x
        

    def draw_sputtering(self):
     
         pygame.draw.rect(self.screen,self.color,self.rect)