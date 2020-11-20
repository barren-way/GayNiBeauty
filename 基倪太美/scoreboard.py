import pygame.font


class Scoreboard():
    def __init__(self,ai_setting,screen,stats,cong,qzgs):
        self.screen=screen
        self.screen_rect = screen.get_rect()
        self.ai_setting =ai_setting
        self.stats=stats
        
        self.text_color=(0,255,0)
        self.text_color_red=(255,0,0)
        self.text_color_yellow=(255,255,0)
        self.text_color_black=(255,255,255)
        self.font =pygame.font.SysFont(None,48)
        self.font_big =pygame.font.Font('image/宋体.ttf',120)
        self.font_middle =pygame.font.SysFont(None,80)
        self.font_title =pygame.font.Font('image/宋体.ttf',180)
        self.font_name =pygame.font.Font('image/宋体.ttf',50)
        

        self.prep_score()
        self.prep_life()
        self.prep_victory(ai_setting)
        
#显示分数
    def prep_score(self):
        score_str=str(self.stats.score)
        self.score_image=self.font.render(score_str,True,self.text_color)
        self.score_rect=self.score_image.get_rect()
        self.score_rect.right=self.screen_rect.right-20
        self.score_rect.top=20

    def show_score(self):
        self.screen.blit(self.score_image,self.score_rect)

#显示命数
    def prep_life(self):
        self.life_color=(0,255,0)
        a='life: '
        
        number_str=str(self.stats.ship_left)
        life_str=a+number_str
        self.life_image=self.font.render(life_str,True,self.life_color)
        self.life_rect=self.life_image.get_rect()
        self.life_rect.right=self.screen_rect.right-50
        self.life_rect.top=700

    def show_life(self):
        self.screen.blit(self.life_image,self.life_rect)

    def prep_cai(self):
        cai_str=str(self.ai_setting.cai_life)
        self.life_image=self.font.render(cai_str,True,self.text_color)
        self.life_rect=self.life_image.get_rect()
        self.life_rect.right=self.screen_rect.right-100
        self.life_rect.top=100

    def show_cai(self):
        self.screen.blit(self.life_image,self.life_rect)


#显示通关
    def prep_victory(self,ai_setting):
        victory='Round 2'
        victory2='Fight!!'
        if ai_setting.time<200:
            victory_str=str(victory)
        else:
            victory_str=str(victory2)

        self.victory_image=self.font_big.render(victory_str,True,self.text_color_red)
        self.victory_rect=self.victory_image.get_rect()
        self.victory_rect.center=self.screen_rect.center
        
        

    def show_victory(self):
        self.screen.blit(self.victory_image,self.victory_rect)

#显示死亡

    def prep_die(self):
        die='菜逼倪中原！！'
        die_str=str(die)
        self.die_image=self.font_big.render(die_str,True,self.text_color_red)
        self.die_rect=self.die_image.get_rect()
        self.die_rect.center=self.screen_rect.center


    def show_die(self):
        self.screen.blit(self.die_image,self.die_rect)
 #显示升级   
    def prep_levelup(self):
        levelup='level up!!'
        levelup_str=str(levelup)
        self.levelup_image=self.font_big.render(levelup_str,True,self.text_color_yellow)
        self.levelup_rect=self.levelup_image.get_rect()
        self.levelup_rect.center=self.screen_rect.center
        self.levelup_rect.top=500


    def show_levelup(self):
        self.screen.blit(self.levelup_image,self.levelup_rect)


#显示等级
    def prep_level(self):
        
        a='lv '
        
        number_str=str(self.stats.level)
        level_str=a+number_str
        self.level_image=self.font_middle.render(level_str,True,self.text_color_yellow)
        self.level_rect=self.level_image.get_rect()
        self.level_rect.right=self.screen_rect.right-100
        self.level_rect.top=600

    def show_level(self):
        self.screen.blit(self.level_image,self.level_rect)

    def prep_title(self):
        die='基倪太美'
        die_str=str(die)
        self.die_image=self.font_title.render(die_str,True,self.text_color_yellow)
        self.die_rect=self.die_image.get_rect()
        self.die_rect.center=self.screen_rect.center
        self.die_rect.top=150

    def show_title(self):
        self.screen.blit(self.die_image,self.die_rect)


#显示名称

    def prep_name(self,stats):
        if stats.level==1:
            die='鸡巴倪'
        if stats.level==2:
            die='弟弟倪'
        if stats.level==3:
            die='狗肉倪'
        if stats.level==4:
            die='臭臭倪'
        if stats.level==5:
            die='臭倪'
        if stats.level==6:
            die='倪'
        if stats.level==7:
            die='倪中原'
        if stats.level==8:
            die='大哥倪'
        if stats.level==9:
            die='倪爷'
        die_str=str(die)
        self.die_image=self.font_name.render(die_str,True,self.text_color_black)
        self.die_rect=self.die_image.get_rect()
        self.die_rect.right=self.screen_rect.right-70
        self.die_rect.top=650


    def show_name(self):
        self.screen.blit(self.die_image,self.die_rect)


    def prep_diao(self):
        cai_str=str(self.ai_setting.diao_life)
        self.life_image=self.font.render(cai_str,True,self.text_color)
        self.life_rect=self.life_image.get_rect()
        self.life_rect.right=self.screen_rect.right-100
        self.life_rect.top=100

    def show_diao(self):
        self.screen.blit(self.life_image,self.life_rect)