import sys
import game_funtion as gf

import pygame
from setting import setting
from ship import ship
from bullet import bullet
from pygame.sprite import Group
from alien import Alien
from game_stats import Gamestats
from button import Button
from scoreboard import Scoreboard
from cai import Cai
from basketball import basketball
from music import Music
from blood import blood
from diao import Diao
from abuse import Abuse
from sputtering import Sputtering
from huojian import Huojian
from niao import niao
from money import Money
from xiong import xiong
from qzg import Qzg
from hailang import Hailang
from zbly import Zbly

def run_game():
    pygame.init()
    ai_setting = setting()
    screen=pygame.display.set_mode(
        (ai_setting.screen_width,ai_setting.screen_height))
    pygame.display.set_caption("ji ni tai mei")
    stats = Gamestats(ai_setting)
    ni=ship(ai_setting,screen,stats)
    zeng = niao(ai_setting,screen)
    bullets = Group()
    abuses = Group()
    sputterings = Group()
    bullets_left = Group()
    bullets_right = Group()
    huojians = Group()
    moneyf = Group()
    aliens =Group()
    cong = xiong(ai_setting,screen)
    zbly = Zbly(ai_setting,screen,cong)
    hailangs = Group()
    qzgs = Group()
    gf.creat_fleet(ai_setting,screen,ni,aliens,stats)
    gf.creat_huojian_fleet(ai_setting,screen,huojians)
    gf.creat_hailang_fleet(ai_setting,screen,hailangs)
  
    play_button=Button(ai_setting,screen,"Play")
    sb=Scoreboard(ai_setting,screen,stats,cong,qzgs)
    background=pygame.image.load(r"image/ouxiang.png")
    #重绘子弹
    screen.blit(background,(0,0))
    
    music1=True
    music2=True
    music3=True
    music4=True
    music5=True
    music6=True
    music7=True
    music8=True

    finall_game=True
    
    cai=Cai(ai_setting,screen)
    basketball1=basketball(ai_setting,screen,1.5,1,cai)
    basketball2=basketball(ai_setting,screen,-1.5,-1,cai)
    basketball3=basketball(ai_setting,screen,1,1.5,cai)
    basketball4=basketball(ai_setting,screen,-1,-1.5,cai)
    basketball5=basketball(ai_setting,screen,0.4,2,cai)

    music=Music(ai_setting,screen,cai,stats,sb,gf)

    blood_cai=blood(ai_setting,screen,1500,stats)
    blood_diao=blood(ai_setting,screen,2000,stats)
    blood_xiong=blood(ai_setting,screen,2000,stats)
    blood_zeng=blood(ai_setting,screen,1500,stats)
    pygame.mixer.init()
    pygame.mixer.music.load("image/鸡你太美.mp3")
    pygame.mixer.music.play(-1,0)

    diao=Diao(ai_setting,screen)
    a=0
    b = pow((9-pow(a,2)),0.5)
    c = 100
    d=0
    e=0
    f=pow((9-pow(e,2)),0.5)
    g=0
    number = 0
    number2 = 0
    #主循环
    while True:
        #响应鼠标键盘
        
        gf.check_events(ai_setting,screen,stats,play_button,ni,bullets,aliens,bullets_left,bullets_right,zeng,moneyf,cong,qzgs,zbly)
        image='image/shi.png'
        
        if stats.game_active:
            ni.update()
            
            bullets.update()
            bullets_left.update()
            bullets_right.update()


           

        #删除消失的子弹
            for bullet in bullets.copy():
                if bullet.rect.bottom<=0:
                    bullets.remove(bullet)
            for bullet in bullets_right.copy():
                if bullet.rect.left<=0:
                    bullets_right.remove(bullet)
            for bullet in bullets_left.copy():
                if bullet.rect.right>=1400:
                    bullets_left.remove(bullet)
        
        #更新屏幕
            
       #检测碰撞
            #music.update(cai)
            
            gf.check_bullet_alien_collisions(ai_setting,screen,stats,sb,ni,aliens,bullets,bullets_left,bullets_right)
            gf.update_aliens(ai_setting,stats,screen,ni,aliens,bullets,sb,zeng,moneyf,huojians)
            
            #蔡关卡
            if stats.score>200 and stats.score<600:
                cai.update()
                basketball1.update()
                basketball2.update()
                basketball3.update()
                basketball4.update()
                basketball5.update()
                gf.update_cai(ai_setting,stats,screen,ni,aliens,bullets,sb,cai,bullets_left,bullets_right)
                ai_setting.basketball_now+=1
                if ai_setting.basketball_now>ai_setting.basketball_time:
                    cai.jump_cai(basketball1)
                    
                    if ai_setting.basketball_now>ai_setting.basketball_time*2:
                        cai.jump_cai(basketball2)
                        
                        if ai_setting.basketball_now>ai_setting.basketball_time*3:
                            cai.jump_cai(basketball3)
                            if ai_setting.basketball_now>ai_setting.basketball_time*4:
                                cai.jump_cai(basketball4)
                                if ai_setting.basketball_now>ai_setting.basketball_time*5:
                                    cai.jump_cai(basketball5)
                                    ai_setting.basketball_now=0
                music.update(cai,ni,ai_setting,stats,sb,gf)
                if music1:
                    pygame.mixer.init()
                    pygame.mixer.music.load("image/手写的从前.mp3")
                    pygame.mixer.music.play(-1,0)
                    music1=False
            if stats.score>800:
                if music2:
                    pygame.mixer.init()
                    pygame.mixer.music.load("image/风车.mp3")
                    pygame.mixer.music.play(-1,0)
                    music2=False
            #曾关卡
            if stats.score>900 and stats.score<1500:
                zeng.update()
                moneyf.update(a,b)
                for money in moneyf.copy():
                    if money.rect.top>=750:
                        moneyf.remove(money)
                gf.update_niao(ai_setting,screen,stats,ni,zeng,sb,bullets,bullets_left,bullets_right)
                gf.update_moneyf(ai_setting,screen,stats,ni,zeng,moneyf,zeng,sb,a,b)
                gf.check_bullet_money_collisions(ai_setting,screen,stats,sb,ni,moneyf,bullets,bullets_left,bullets_right)
                gf.update_huojians(ai_setting,stats,screen,zeng,ni,huojians,sb)
                
                a+=10
                if a==100 :
                
                    gf.create_money(ai_setting,screen,stats,zeng,moneyf)
                    a=0
                    ai_setting.money_speed_factor *= -1
                if music3:
                    pygame.mixer.init()
                    pygame.mixer.music.load("image/areyouok.mp3")
                    pygame.mixer.music.play(-1,0)
                    music3=False
            if stats.score>1500:
                if music4:
                    pygame.mixer.init()
                    pygame.mixer.music.load("image/风车.mp3")
                    pygame.mixer.music.play(-1,0)
                    music4=False
            #熊关卡
            if stats.score>1900 and stats.score<2500:
                cong.update()
                qzgs.update()
                zbly.update()
                gf.update_xiong(ai_setting,screen,stats,ni,cong,sb,bullets,bullets_left,bullets_right)
                gf.update_qzgs(ai_setting,screen,stats,ni,qzgs,cong,sb,bullets)
                gf.check_bullet_qzg_collisions(ai_setting,screen,stats,sb,ni,qzgs,bullets)
                gf.update_hailangs(ai_setting,stats,screen,cong,ni,hailangs,sb)
                d+=10
                if d==10000 :
                
                    gf.create_qzg(ai_setting,screen,stats,cong,qzgs)
                    a=0
                    #ai_setting.qzg_speed_factor *= -1
                    for qzg in qzgs:
                        number+=1
                        if stats.ship_left>0:
                            stats.ship_left-=1*number
                            sb.prep_life()
                        else:
                            stats.game_active=False
                            pygame.mouse.set_visible(True)
                if music5:
                    pygame.mixer.init()
                    pygame.mixer.music.load("image/滑板鞋.mp3")
                    pygame.mixer.music.play(-1,0)
                    music5=False
                            
            if stats.score>2500:
                if music6:
                    pygame.mixer.init()
                    pygame.mixer.music.load("image/骚猪.mp3")
                    pygame.mixer.music.play(-1,0)
                    music6=False               
            #吊关卡
            if stats.score>3100 and stats.score<4000:
                diao.update()
                ai_setting.abuse_time+=1
                if ai_setting.abuse_time==ai_setting.diao_speed:
                    image='image/nmsl.png'
                    new_abuse = Abuse(ai_setting,screen,ship,0,1,stats,diao,image)
                    abuses.add(new_abuse)
                    image='image/cnm.png'
                    new_abuse = Abuse(ai_setting,screen,ship,0.7,0.7,stats,diao,image)
                    abuses.add(new_abuse)
                    new_abuse = Abuse(ai_setting,screen,ship,-0.7,0.7,stats,diao,image)
                    abuses.add(new_abuse)
                    image='image/yashi.png'
                    new_abuse = Abuse(ai_setting,screen,ship,1,0,stats,diao,image)
                    abuses.add(new_abuse)
                    new_abuse = Abuse(ai_setting,screen,ship,-1,0,stats,diao,image)
                    image='image/mmp.png'
                    abuses.add(new_abuse)
                    new_abuse = Abuse(ai_setting,screen,ship,0.4,0.8,stats,diao,image)
                    abuses.add(new_abuse)
                    new_abuse = Abuse(ai_setting,screen,ship,-0.4,0.8,stats,diao,image)
                    abuses.add(new_abuse)
                    new_abuse = Abuse(ai_setting,screen,ship,0.8,0.4,stats,diao,image)
                    abuses.add(new_abuse)
                    new_abuse = Abuse(ai_setting,screen,ship,-0.8,0.4,stats,diao,image)
                    abuses.add(new_abuse)
                    image='image/nmsl.png'
                    new_abuse = Abuse(ai_setting,screen,ship,0.95,0.2,stats,diao,image)
                    abuses.add(new_abuse)
                    new_abuse = Abuse(ai_setting,screen,ship,-0.95,0.2,stats,diao,image)
                    abuses.add(new_abuse)
                    ai_setting.abuse_time=0
                    if ai_setting.diao_speed>=150 :
                        ai_setting.diao_speed-=5
                    if ai_setting.diao_speed>=80 and  ai_setting.diao_speed<150:
                        ai_setting.diao_speed-=2 
                    if ai_setting.diao_speed>=15 and  ai_setting.diao_speed<80:
                        ai_setting.diao_speed-=1
                if music7:
                    pygame.mixer.init()
                    pygame.mixer.music.load("image/五五开.mp3")
                    pygame.mixer.music.play(-1,0)
                    music7=False
            if stats.score>3500:
                zbly.update()
                if finall_game:
                    ai_setting.diao_life=100000
                    stats.xiong_left=500000
                    ai_setting.cai_life=100000
                    ai_setting.niao_life=100000
                    finall_game=False
                if music8:
                    pygame.mixer.init()
                    pygame.mixer.music.load("image/一剪梅.mp3")
                    pygame.mixer.music.play(-1,0)
                    music8=False
                if stats.score>3500:
                    cai.update()
                    #zeng.update()
                    basketball1.update()
                    basketball2.update()
                    basketball3.update()
                    basketball4.update()
                    basketball5.update()
                    gf.update_cai(ai_setting,stats,screen,ni,aliens,bullets,sb,cai,bullets_left,bullets_right)
                    ai_setting.basketball_now+=1
                    if ai_setting.basketball_now>ai_setting.basketball_time:
                        cai.jump_cai(basketball1)
                    
                        if ai_setting.basketball_now>ai_setting.basketball_time*2:
                            cai.jump_cai(basketball2)
                        
                            if ai_setting.basketball_now>ai_setting.basketball_time*3:
                                cai.jump_cai(basketball3)
                                if ai_setting.basketball_now>ai_setting.basketball_time*4:
                                    cai.jump_cai(basketball4)
                                    if ai_setting.basketball_now>ai_setting.basketball_time*5:
                                        cai.jump_cai(basketball5)
                                        ai_setting.basketball_now=0
                    music.update(cai,ni,ai_setting,stats,sb,gf)
                   #zeng
                    moneyf.update(a,b)
                    for money in moneyf.copy():
                        if money.rect.top>=750:
                            moneyf.remove(money)
                    gf.update_niao(ai_setting,screen,stats,ni,zeng,sb,bullets,bullets_left,bullets_right)
                    gf.update_moneyf(ai_setting,screen,stats,ni,zeng,moneyf,zeng,sb,a,b)
                    gf.check_bullet_money_collisions(ai_setting,screen,stats,sb,ni,moneyf,bullets,bullets_left,bullets_right)
                    gf.update_huojians(ai_setting,stats,screen,zeng,ni,huojians,sb)
                    e+=10
                    if e==100 :
                
                        gf.create_money(ai_setting,screen,stats,zeng,moneyf)
                        e=0
                        ai_setting.money_speed_factor *= -1
                #else:
                    diao.update()
                    cong.update()
                    ai_setting.abuse_time+=1
                    if ai_setting.abuse_time==ai_setting.diao_speed:
                        image='image/nmsl.png'
                        new_abuse = Abuse(ai_setting,screen,ship,0,1,stats,diao,image)
                        abuses.add(new_abuse)
                        image='image/cnm.png'
                        new_abuse = Abuse(ai_setting,screen,ship,0.7,0.7,stats,diao,image)
                        abuses.add(new_abuse)
                        new_abuse = Abuse(ai_setting,screen,ship,-0.7,0.7,stats,diao,image)
                        abuses.add(new_abuse)
                        image='image/yashi.png'
                        new_abuse = Abuse(ai_setting,screen,ship,1,0,stats,diao,image)
                        abuses.add(new_abuse)
                        new_abuse = Abuse(ai_setting,screen,ship,-1,0,stats,diao,image)
                        image='image/mmp.png'
                        abuses.add(new_abuse)
                        new_abuse = Abuse(ai_setting,screen,ship,0.4,0.8,stats,diao,image)
                        abuses.add(new_abuse)
                        new_abuse = Abuse(ai_setting,screen,ship,-0.4,0.8,stats,diao,image)
                        abuses.add(new_abuse)
                        new_abuse = Abuse(ai_setting,screen,ship,0.8,0.4,stats,diao,image)
                        abuses.add(new_abuse)
                        new_abuse = Abuse(ai_setting,screen,ship,-0.8,0.4,stats,diao,image)
                        abuses.add(new_abuse)
                        image='image/nmsl.png'
                        new_abuse = Abuse(ai_setting,screen,ship,0.95,0.2,stats,diao,image)
                        abuses.add(new_abuse)
                        new_abuse = Abuse(ai_setting,screen,ship,-0.95,0.2,stats,diao,image)
                        abuses.add(new_abuse)
                        ai_setting.abuse_time=0
                        if ai_setting.diao_speed>=150 :
                            ai_setting.diao_speed-=5
                        if ai_setting.diao_speed>=80 and  ai_setting.diao_speed<150:
                            ai_setting.diao_speed-=2 
                        if ai_setting.diao_speed>=15 and  ai_setting.diao_speed<80:
                            ai_setting.diao_speed-=1
                    qzgs.update()
                    
                    gf.update_xiong(ai_setting,screen,stats,ni,cong,sb,bullets,bullets_left,bullets_right)
                    gf.update_qzgs(ai_setting,screen,stats,ni,qzgs,cong,sb,bullets)
                    gf.check_bullet_qzg_collisions(ai_setting,screen,stats,sb,ni,qzgs,bullets)
                    gf.update_hailangs(ai_setting,stats,screen,cong,ni,hailangs,sb)
                    g+=10
                    if g==10000 :
                
                        gf.create_qzg(ai_setting,screen,stats,cong,qzgs)
                        a=0
                        #ai_setting.qzg_speed_factor *= -1
                        for qzg in qzgs:
                            number2+=1
                            if stats.ship_left>0:
                                stats.ship_left-=1*number2
                                sb.prep_life()
                            else:
                                stats.game_active=False
                                pygame.mouse.set_visible(True)

        gf.update_screen(ai_setting,screen,stats,ni,aliens,bullets,play_button,sb,cai,basketball1,basketball2,basketball3,basketball4,basketball5,music,bullets_left,bullets_right,blood_cai,diao,abuses,sputterings,blood_diao,zeng,moneyf,huojians,cong,qzgs,hailangs,zbly,blood_zeng,blood_xiong,bullets)
        
    else:
        sb.prep_die()
        sb.show_die()
run_game()
