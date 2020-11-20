import pygame


class setting():
    def __init__(self):
        self.screen_width=1400
        self.screen_height=750
        self.bg_color=(40,0,100)

        self.ship_speed_factor =3
        self.ship_limit=25000

        #计时器
        self.time=0
        self.levelup_time=0
        self.level_up=False
        self.levelup_time2=0
        self.level_up2=False
        self.levelup_time3=0
        self.level_up3=False
        self.levelup_time4=0
        self.level_up4=False
        self.levelup_time5=0
        self.level_up5=False
        self.levelup_time6=0
        self.level_up6=False
        self.levelup_time7=0
        self.level_up7=False
        self.levelup_time8=0
        self.level_up8=False

        self.abuse_time=1
        self.recover_time=1

        #子弹设置
        self.bullet_speed_factor=5
        self.bullet_width=5
        self.bullet_height=15
        self.bullet_color=(255,255,255)
        self.bullet_allowed=4


        #外星人设置
        self.alien_speed_factor=2
        #外星人向下移动距离
        self.fleet_drop_speed=90
        #方向
        self.fleet_direction=1
        #外星人分数
        self.alien_point=1


        self.cai_speed=3
        self.cai_direction=1
        self.cai_life=1500
        #蔡yinyve伤害
        self.cai_big=40
        self.cai_music=5
        
        self.basketball_allowed=5
        self.basketball_damage=1
        self.basketball_number=0
        self.basketball_speed=3
        #蔡跳到篮球的时间
        self.basketball_time=200
 
        self.basketball_now=0


        #关卡分数
        self.score_2=600


        self.sputtering_width=10
        self.sputtering_height=10
        


        #diao
        self.diao_life=1000
        self.diao_image=20
        self.diao_speed=350

        #曾
        self.niao_speed_factor=3
        self.fleet_direction_zeng=1
        self.niao_life=1500
        
        

        #钱
        self.money_speed_factor=1
        self.money_allowed=60
        self.fleet_drop_speed_money=1
        
        self.huojian_speed_factor = 0
        self.time_huojian1=0
        self.time_huojian2=0

        #qzg
        self.qzg_speed_factor=6
        self.qzg_allowed=2
        self.fleet_direction_qzg = 1
        self.Qzg_limit=5

        #海浪
        self.hailang_speed_factor = 0

        #自闭领域
        self.zbly_speed_factor=1
        self.zbly_fleet_direction = 1

        #熊
        self.xiong_speed_factor=3
        self.xiong_limit=2000
        self.fleet_direction_cong=1
        self.time_zbly1=0
        self.time_zbly2=0
        self.time_hailang1=0
        self.time_hailang2=0
        self.time_xiong1=0
        self.time_xiong2=0