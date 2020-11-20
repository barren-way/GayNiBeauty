import pygame
from pygame.sprite import Sprite
from ship import ship


class bullet(Sprite):
    def __init__(self,ai_setting,screen,ship,x,y,stats):
        super(bullet,self).__init__()
        self.screen=screen
        if stats.level<5:
            self.image =pygame.image.load('image/shi.png')
        if stats.level<8:
            self.image =pygame.image.load('image/dashi.png')
        else:
            self.image =pygame.image.load('image/dadashi.png')
        if stats.level>=4:
            
            self.rect =self.image.get_rect()
            self.screen_rect=screen.get_rect()
        else:
            if x==0:
                self.rect = pygame.Rect(0,0,ai_setting.bullet_width,ai_setting.bullet_height)
            else:
                self.rect = pygame.Rect(0,0,ai_setting.bullet_height,ai_setting.bullet_width)
        self.rect.centerx=ship.rect.centerx
        self.rect.top=ship.rect.top
        self.y=float(self.rect.y)
        self.x=float(self.rect.x)

        self.color = ai_setting.bullet_color
        self.speed_factor = ai_setting.bullet_speed_factor

        self.direction_x=x
        self.direction_y=y
    def update(self):
        self.y-=self.speed_factor*self.direction_y
        self.x-=self.speed_factor*self.direction_x
        self.rect.y=self.y
        self.rect.x=self.x
        

    def draw_bullet(self,stats):
        if stats.level>=4:
            self.screen.blit(self.image,self.rect)
        else:
            pygame.draw.rect(self.screen,self.color,self.rect)