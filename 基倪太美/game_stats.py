import pygame

class Gamestats():
    def __init__(self,ai_setting):
        self.ai_setting=ai_setting
        self.reset_stats(ai_setting)
        self.game_active=False
        self.ship_left = self.ai_setting.ship_limit
        self.level=1
        self.score=0
        self.first_play=True
        self.xiong_left = self.ai_setting.xiong_limit
        self.Qzg_left = self.ai_setting.Qzg_limit
    def reset_stats(self,ai_setting):
        self.ship_left = self.ai_setting.ship_limit
        self.xiong_left = self.ai_setting.xiong_limit
        self.Qzg_left = self.ai_setting.Qzg_limit
        self.score=0 
        
