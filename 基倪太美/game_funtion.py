import sys
import pygame
from bullet import bullet
from alien import Alien
from time import sleep
from abuse import Abuse
from sputtering import Sputtering
from niao import niao
from huojian import Huojian
from xiong import xiong
from qzg import Qzg
from hailang import Hailang
from zbly import Zbly
from money import Money

#键盘响应函数
def check_events(ai_setting,screen,stats,play_button,ship,bullets,aliens,bullets_left,bullets_right,zeng,moneyf,cong,qzgs,zbly):
    
    for event in pygame.event.get():
        if  event.type == pygame.QUIT:
            sys.exit()

        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y=pygame.mouse.get_pos()
            check_play_button(stats,play_button,mouse_x,mouse_y,aliens,bullets,ship,ai_setting,screen)
            stats.first_play=False
        #按下方向按钮
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right=True
            if event.key ==pygame.K_LEFT:
                ship.moving_left=True
            if event.key == pygame.K_UP:
                ship.moving_up=True
            if event.key == pygame.K_DOWN:
                ship.moving_down=True
            #创建子弹
            if event.key == pygame.K_SPACE:
                if len(bullets) < ai_setting.bullet_allowed:
                    new_bullet = bullet(ai_setting,screen,ship,0,1,stats)
                    if stats.level>1:
                        new_bullet_left = bullet(ai_setting,screen,ship,-1,0,stats)
                        new_bullet_right = bullet(ai_setting,screen,ship,1,0,stats)
                        bullets_left.add(new_bullet_left)
                        bullets_right.add(new_bullet_right)
                    bullets.add(new_bullet)
                    


        #松开 方向按钮
        elif event.type ==pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right =False
            if event.key==pygame.K_LEFT:
                ship.moving_left =False
            if event.key == pygame.K_UP:
                ship.moving_up =False
            if event.key == pygame.K_DOWN:
                ship.moving_down =False
       



def update_screen(ai_setting,screen,stats,ni,aliens,bullet,
                  play_button,sb,cai,basketball1,basketball2,basketball3,basketball4,basketball5,music,bullets_left,bullets_right,blood_cai,diao,abuses,sputterings,blood_diao,zeng,moneyf,huojians,cong,qzgs,hailangs,zbly,blood_zeng,blood_xiong,bullets):
    screen.fill(ai_setting.bg_color)
    #重绘子弹
    
    
    
    #吊关卡
    if stats.score>3100 and stats.score<3500:
        
        
        diao.blitme()
        for abuse in abuses.sprites():
            abuse.draw_abuse()
            abuse.update()
        abuse_sputter(abuses,sputterings,screen,ai_setting,stats,ni,sb)
        for sputtering in sputterings.sprites():
            sputtering.draw_sputtering()
            sputtering.update()
        sb.prep_diao()
        sb.show_diao()    
        update_diao(ai_setting,stats,screen,ni,aliens,bullet,sb,diao,bullets_left,bullets_right)   
        diao_recover(ai_setting)
        blood_diao.draw_blood(ai_setting,stats)
    #曾关卡
    if stats.score>900 and stats.score<1500:
        
        zeng.blitme()
        moneyf.draw(screen)
        blood_zeng.draw_blood(ai_setting,stats)
        #if stats.score>1200 or stats.score>2000:
        ai_setting.time_huojian1+=1
        if ai_setting.time_huojian1>1000:

            huojians.draw(screen)
            ai_setting.huojian_speed_factor = 3
            ai_setting.time_huojian2+=1
            if ai_setting.time_huojian2==1000:
                ai_setting.time_huojian1=0
                ai_setting.time_huojian2=0
        else:
            ai_setting.huojian_speed_factor=0
        

    #熊关卡
    if stats.score>1900and stats.score<2500:
        #if stats.score>2000 and stats.score<2300:
        
        
        ai_setting.time_zbly1+=1
        if ai_setting.time_zbly1 >= 500:
            zbly.blitme()
            zbly_ship_hit(ai_setting,screen,stats,zbly,ni,sb)
            ai_setting.time_zbly2+=1
            if ai_setting.time_zbly2==500:
                ai_setting.time_zbly1 =0
                ai_setting.time_zbly2==0

        #if stats.score>2200 or stats.score>2400:
        ai_setting.time_hailang1+=1
        if ai_setting.time_hailang1>600:
            hailangs.draw(screen)
            ai_setting.hailang_speed_factor = 3
            ai_setting.time_hailang2+=1
            if ai_setting.time_hailang2==100:
                ai_setting.time_hailang2==0
                ai_setting.time_hailang1=0
        cong.blitme()
        qzgs.draw(screen)
        blood_xiong.draw_blood(ai_setting,stats)
        #if stats.score>1600:
        ai_setting.time_xiong1+=1
        if ai_setting.time_xiong1>500:
            
            ai_setting.xiong_speed_factor=0
            ai_setting.time_xiong2+=1
            if ai_setting.time_xiong2==500:
                ai_setting.time_xiong1=0
                ai_setting.time_xiong2=0
 
        else:
            ai_setting.xiong_speed_factor=3
            
        if pygame.sprite.spritecollideany(ni,hailangs):
            ai_setting.hailang_speed_factor = 0

            sb.show_score()                
            sb.show_life()
        #if stats.score>100:
            #sb.show_xiong_life()

    #蔡关卡
    if stats.score>200 and stats.score<600:
        
        music.blitme()
        cai.blitme()
        
        update_basketball(basketball1,ni,ai_setting,stats,screen,aliens,bullet,sb)
        update_basketball(basketball2,ni,ai_setting,stats,screen,aliens,bullet,sb)
        update_basketball(basketball3,ni,ai_setting,stats,screen,aliens,bullet,sb)
        update_basketball(basketball4,ni,ai_setting,stats,screen,aliens,bullet,sb)
        update_basketball(basketball5,ni,ai_setting,stats,screen,aliens,bullet,sb)
        sb.prep_cai()
        sb.show_cai()
        blood_cai.draw_blood(ai_setting,stats)
    #最后一波
    if stats.score>3500 :
        if stats.score>3500:
            ai_setting.time_zbly1+=1
            if ai_setting.time_zbly1 >= 500:
                zbly.blitme()
                zbly_ship_hit(ai_setting,screen,stats,zbly,ni,sb)
                ai_setting.time_zbly2+=1
                if ai_setting.time_zbly2==500:
                    ai_setting.time_zbly1 =0
                    ai_setting.time_zbly2==0
            music.blitme()
            cai.blitme()
            zeng.blitme()
            update_basketball(basketball1,ni,ai_setting,stats,screen,aliens,bullet,sb)
            update_basketball(basketball2,ni,ai_setting,stats,screen,aliens,bullet,sb)
            update_basketball(basketball3,ni,ai_setting,stats,screen,aliens,bullet,sb)
            update_basketball(basketball4,ni,ai_setting,stats,screen,aliens,bullet,sb)
            update_basketball(basketball5,ni,ai_setting,stats,screen,aliens,bullet,sb)
            sb.prep_cai()
            sb.show_cai()
            blood_cai.draw_blood(ai_setting,stats)

            #zeng.blitme()
            moneyf.draw(screen)
            blood_zeng.draw_blood(ai_setting,stats)
            #if stats.score>1200 or stats.score>2000:
            ai_setting.time_huojian1+=1
            if ai_setting.time_huojian1>1000:

                huojians.draw(screen)
                ai_setting.huojian_speed_factor = 3
                ai_setting.time_huojian2+=1
                if ai_setting.time_huojian2==1000:
                    ai_setting.time_huojian1=0
                    ai_setting.time_huojian2=0
            else:
                ai_setting.huojian_speed_factor=0
        #else:
            diao.blitme()
            #cong.blitme()
            for abuse in abuses.sprites():
                abuse.draw_abuse()
                abuse.update()
            abuse_sputter(abuses,sputterings,screen,ai_setting,stats,ni,sb)
            for sputtering in sputterings.sprites():
                sputtering.draw_sputtering()
                sputtering.update()
            sb.prep_diao()
            sb.show_diao()    
            update_diao(ai_setting,stats,screen,ni,aliens,bullet,sb,diao,bullets_left,bullets_right)   
            diao_recover(ai_setting)
            blood_diao.draw_blood(ai_setting,stats)

            

            #if stats.score>2200 or stats.score>2400:
            ai_setting.time_hailang1+=1
            if ai_setting.time_hailang1>600:
                hailangs.draw(screen)
                ai_setting.hailang_speed_factor = 3
                ai_setting.time_hailang2+=1
                if ai_setting.time_hailang2==100:
                    ai_setting.time_hailang2==0
                    ai_setting.time_hailang1=0
            cong.blitme()
            qzgs.draw(screen)
            blood_xiong.draw_blood(ai_setting,stats)

            #if stats.score>1600:
            ai_setting.time_xiong1+=1
            if ai_setting.time_xiong1>500:
            
                ai_setting.xiong_speed_factor=0
                ai_setting.time_xiong2+=1
                if ai_setting.time_xiong2==500:
                    ai_setting.time_xiong1=0
                    ai_setting.time_xiong2=0
 
            else:
                ai_setting.xiong_speed_factor=3
            
            if pygame.sprite.spritecollideany(ni,hailangs):
                ai_setting.hailang_speed_factor = 0

                sb.show_score()                
                sb.show_life()
    
    aliens.draw(screen)
    sb.show_score()
    sb.prep_life()
    sb.show_life()
    sb.prep_level()
    sb.show_level()
    sb.prep_name(stats)
    sb.show_name()
    check_level(stats,sb,ai_setting)

    if stats.score>ai_setting.score_2 and ai_setting.time<400:
          
        ai_setting.time+=1
        sb.prep_victory(ai_setting)
        sb.show_victory()
    ni.blitme(stats)
    for bullet in bullet.sprites():
        bullet.draw_bullet(stats)
    for bullet in bullets_left.sprites():
        bullet.draw_bullet(stats)
    for bullet in bullets_right.sprites():
        bullet.draw_bullet(stats)
    if not stats.game_active:
        play_button.draw_button()
        
        if not stats.first_play:    
            sb.prep_die()
            sb.show_die()
        else:
            sb.prep_title()
            sb.show_title()
    pygame.display.flip()
    


#计算每行每列外星人数量
def get_number_aliens_x(ai_setting,alien_width):
    available_space_x = ai_setting.screen_width-2*alien_width
    number_aliens_x = int(available_space_x/(2*alien_width))
    return number_aliens_x

def get_number_rows(ai_setting,ship_height,alien_height):
    available_space_y = (ai_setting.screen_height-
                         (3* alien_height) -ship_height)
    number_rows = int(available_space_y/(2* alien_height))
    return number_rows



def creat_onealien(ai_setting,screen,aliens,alien_number,row_number,stats):
    alien=Alien(ai_setting,screen,stats)
    alien_width=alien.rect.width
    alien_height=alien.rect.height
    if ai_setting.fleet_direction == -1:
        alien.x =ai_setting.screen_width-alien_width-2 * alien_width * alien_number
    if ai_setting.fleet_direction == 1:
        alien.x =2*alien_width * (alien_number+1)-1*alien_width
    alien.rect.y =alien_height+2* alien.rect.height * (row_number-1)
    alien.rect.x=alien.x
    aliens.add(alien)

#创建一群外星人
def creat_alien(ai_setting,screen,aliens,alien_number,row_number,stats):
    alien=Alien(ai_setting,screen,stats)
    alien_width=alien.rect.width
    alien_height=alien.rect.height
    alien.x =alien_width+2 * alien_width * alien_number
    alien.rect.y =alien_height+2* alien.rect.height * row_number
    alien.rect.x=alien.x
    aliens.add(alien)



def creat_onefleet(ai_setting,screen,ship,aliens,row_number,stats):
    alien=Alien(ai_setting,screen,stats)
    number_aliens_x=get_number_aliens_x(ai_setting,alien.rect.width)
    number_rows=get_number_rows(ai_setting,ship.rect.height,alien.rect.height)
    
    #一行放置外星人数量
    for row_number in range(row_number):
        for alien_number in range(number_aliens_x):
            creat_onealien(ai_setting,screen,aliens,alien_number,row_number,stats)

#创建外星人群
def creat_fleet(ai_setting,screen,ship,aliens,stats):
    alien=Alien(ai_setting,screen,stats)
    number_aliens_x=get_number_aliens_x(ai_setting,alien.rect.width)
    number_rows=get_number_rows(ai_setting,ship.rect.height,alien.rect.height)
    
    #一行放置外星人数量
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            creat_alien(ai_setting,screen,aliens,alien_number,row_number,stats)

#刷新外星人
def update_aliens(ai_setting,stats,screen,ship,aliens,bullets,sb,niao,moneyf,xiong):
    check_fleet_edges(ai_setting,screen,ship,aliens,bullets,stats)
    aliens.update()
    if len(aliens)==0:
        creat_fleet(ai_setting,screen,ship,aliens,stats)
    if pygame.sprite.spritecollideany(ship,aliens):
        
        ship_hit(ai_setting,stats,screen,ship,aliens,bullets,sb,niao,moneyf,xiong)
    check_aliens_bottom(ai_setting,stats,screen,ship,aliens,bullets,sb,niao,moneyf,xiong)
        

#判断外星人是否到达边缘
def check_fleet_edges(ai_setting,screen,ship,aliens,bullets,stats):
    
    alien=Alien(ai_setting,screen,stats)
    number_aliens_x=get_number_aliens_x(ai_setting,alien.rect.width)
    for alien in aliens.sprites():
        if alien.check_edges():
            
            change_fleet_direction(ai_setting,screen,ship,aliens,stats)
            #if len(aliens)<=10:
               # creat_onefleet(ai_setting,screen,ship,aliens,3,stats)
            if len(aliens)<=15:
                creat_onefleet(ai_setting,screen,ship,aliens,2,stats)
            if len(aliens)<=30:
                creat_onefleet(ai_setting,screen,ship,aliens,1,stats)
         
            

            break

#外星人下移，改变方向
def change_fleet_direction(ai_setting,screen,ship,aliens,stats):
    
    alien=Alien(ai_setting,screen,stats)
    number_aliens_x=get_number_aliens_x(ai_setting,alien.rect.width)
    for alien in aliens.sprites():
        alien.rect.y+=ai_setting.fleet_drop_speed
     
        
    ai_setting.fleet_direction*=-1


#飞船和外星人碰撞
def ship_hit(ai_setting,stats,screen,ship,aliens,bullets,sb,niao,moneyf,xiong):
    if stats.ship_left>0:
        stats.ship_left-=1
        sb.prep_life()
       
        #aliens.empty()
        #bullets.empty()
        #creat_fleet(ai_setting,screen,ship,aliens)
        #ship.center_ship()
        #sleep(0.5)
    else:
        ni_die(stats,sb,ai_setting)
        

    #检查外星人是否到达屏幕底
def check_aliens_bottom(ai_setting,stats,screen,ship,aliens,bullets,sb,niao,moneyf,xiong):
    screen_rect=screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom>=screen_rect.bottom:
            aliens.remove(alien)
            stats.ship_left-=500
            sb.prep_life()
            ship_hit(ai_setting,stats,screen,ship,aliens,bullets,sb,niao,moneyf,xiong)
            break
    
#判断鼠标点击开始按钮
def check_play_button(stats,play_button,mouse_x,mouse_y,aliens,bullets,ship,ai_setting,screen):
    button_clicked=play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active:
        pygame.mouse.set_visible(False)
        stats.game_active=True
        stats.reset_stats(ai_setting)
        aliens.empty()
        bullets.empty()
        creat_fleet(ai_setting,screen,ship,aliens,stats)
        ship.center_ship()


def check_bullet_alien_collisions(ai_setting,screen,stats,sb,ship,aliens,bullets,bullets_left,bullets_right):
    if stats.level<9:
        collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
    else:
        collisions = pygame.sprite.groupcollide(bullets,aliens,False,True)
    collisions_right = pygame.sprite.groupcollide(bullets_right,aliens,True,True)
    collisions_left = pygame.sprite.groupcollide(bullets_left,aliens,True,True)
    if collisions:
        stats.score+=ai_setting.alien_point
        sb.prep_score()
    if collisions_right:
        stats.score+=ai_setting.alien_point
        sb.prep_score()
    if collisions_left:
        stats.score+=ai_setting.alien_point
        sb.prep_score()


        #刷新蔡
def update_cai(ai_setting,stats,screen,ship,aliens,bullets,sb,cai,bullets_left,bullets_right):
    cai.update()
    if pygame.sprite.spritecollideany(cai,bullets):
        cai_hit(ai_setting,stats,screen,ship,cai,bullets,sb)
    if pygame.sprite.spritecollideany(cai,bullets_left):
        cai_hit(ai_setting,stats,screen,ship,cai,bullets,sb)
    if pygame.sprite.spritecollideany(cai,bullets_right):
        cai_hit(ai_setting,stats,screen,ship,cai,bullets,sb)
    if pygame.Rect.colliderect(cai.rect,ship.rect):
        if stats.ship_left>0:
            stats.ship_left-=ai_setting.cai_big
            sb.prep_life()
        else:
            stats.game_active=False
            pygame.mouse.set_visible(True)
            
        
    

#蔡被打
def cai_hit(ai_setting,stats,screen,ship,cai,bullets,sb):
    if ai_setting.cai_life>0:
        ai_setting.cai_life-=1
        sb.prep_cai()
        
       
        #aliens.empty()
        #bullets.empty()
        #creat_fleet(ai_setting,screen,ship,aliens)
        #ship.center_ship()
        #sleep(0.5)
    else:
        stats.score=ai_setting.score_2
        


#刷新篮球
def update_basketball(basketball,ship,ai_setting,stats,screen,aliens,bullets,sb):
    basketball.draw_basketball()
    if pygame.Rect.colliderect(basketball.rect, ship.rect):
        if stats.ship_left>0:
            stats.ship_left-=ai_setting.basketball_damage
            sb.prep_life()
       
        #aliens.empty()
        #bullets.empty()
        #creat_fleet(ai_setting,screen,ship,aliens)
        #ship.center_ship()
        #sleep(0.5)
        else:
            ni_die(stats,sb,ai_setting)
        

#判断等级
def check_level(stats,sb,ai_setting):
    
    
    if stats.score>100and stats.score<600:
        if ai_setting.levelup_time==0:
            ai_setting.level_up=True
        if ai_setting.level_up:
            sb.prep_levelup()
            sb.show_levelup()
            ai_setting.levelup_time+=1
            if ai_setting.levelup_time>300:
                ai_setting.level_up=False

        stats.level=2
    if stats.score>600 and stats.score<800:
        if ai_setting.levelup_time2==0:
            ai_setting.level_up2=True
            stats.ship_left+=25000
        if ai_setting.level_up2:
            sb.prep_levelup()
            sb.show_levelup()
            ai_setting.bullet_speed_factor=12
            ai_setting.levelup_time2+=1
            if ai_setting.levelup_time2>300:
                ai_setting.level_up2=False
        stats.level=3
    if stats.score>=800:
        if ai_setting.levelup_time3==0:
            ai_setting.level_up3=True
        if ai_setting.level_up3:
            sb.prep_levelup()
            sb.show_levelup()
            ai_setting.levelup_time3+=1
            if ai_setting.levelup_time3>300:
                ai_setting.level_up3=False
        stats.level=4
    if stats.score>=1500:
        if ai_setting.levelup_time4==0:
            ai_setting.level_up4=True
            stats.ship_left+=30000
        if ai_setting.level_up4:
            sb.prep_levelup()
            sb.show_levelup()
            ai_setting.levelup_time4+=1
            if ai_setting.levelup_time4>300:
                ai_setting.level_up4=False
        stats.level=5
        #6级打熊
    if stats.score>=1800:
        if ai_setting.levelup_time5==0:
            ai_setting.level_up5=True
        if ai_setting.level_up5:
            ai_setting.ship_speed_factor =6
            sb.prep_levelup()
            sb.show_levelup()
            ai_setting.levelup_time5+=1
            if ai_setting.levelup_time5>300:
                ai_setting.level_up5=False
        stats.level=6
    
    if stats.score>=2500:
        if ai_setting.levelup_time6==0:
            ai_setting.level_up6=True
            stats.ship_left+=30000
        if ai_setting.level_up6:
            sb.prep_levelup()
            sb.show_levelup()
            ai_setting.levelup_time6+=1
            if ai_setting.levelup_time6>300:
                ai_setting.level_up6=False
        stats.level=7
    #8级打吊
    if stats.score>=2900:
        if ai_setting.levelup_time7==0:
            ai_setting.level_up7=True
        if ai_setting.level_up7:
            sb.prep_levelup()
            sb.show_levelup()
            ai_setting.levelup_time7+=1
            if ai_setting.levelup_time7>300:
                ai_setting.level_up7=False
        stats.level=8

    if stats.score>=4000:
        if ai_setting.levelup_time8==0:
            ai_setting.level_up8=True
            stats.ship_left+=100000
        if ai_setting.level_up7:
            sb.prep_levelup()
            sb.show_levelup()
            ai_setting.levelup_time8+=1
            if ai_setting.levelup_time8>300:
                ai_setting.level_up8=False
        stats.level=9
        
        

#死亡
def ni_die(stats,sb,ai_setting):
    stats.game_active=False
    pygame.mouse.set_visible(True)
    if not stats.game_active:
        sb.prep_die()
        sb.show_die()




#判断溅射遇到屏幕边缘
def sputtering_miss(screen,sputterings):
    screen_rect=screen.get_rect()
    for sputtering in sputterings.copy():
        if sputtering.rect.bottom>=screen_rect.bottom:
            sputterings.remove(sputtering)
            
        if sputtering.rect.right>=screen_rect.right:
            sputterings.remove(sputtering)
        if sputtering.rect.left<=0:
            sputterings.remove(sputtering)


#判断喷人到边缘
def abuse_sputter(abuses,sputterings,screen,ai_setting,stats,ship,sb):
    screen_rect=screen.get_rect()
    for abuse in abuses.copy():
        if abuse.rect.bottom>=screen_rect.bottom:
            abuses.remove(abuse)
            sputter(sputterings,abuse,ai_setting,screen,stats)
        if abuse.rect.right>=screen_rect.right:
            sputter(sputterings,abuse,ai_setting,screen,stats)
            abuses.remove(abuse)
        if abuse.rect.left<=0:
            sputter(sputterings,abuse,ai_setting,screen,stats)
            abuses.remove(abuse)
    sputtering_miss(screen,sputterings)
    if pygame.sprite.spritecollideany(ship,abuses):
        if stats.ship_left>0:
            ai_setting.diao_life+=2
            stats.ship_left-=10
       
        else:
            ni_die(stats,sb,ai_setting)
        
    if pygame.sprite.spritecollideany(ship,sputterings):
        if stats.ship_left>0:
            stats.ship_left-=8
        else:
            ni_die(stats,sb,ai_setting)
#溅射
def sputter(sputterings,abuse,ai_setting,screen,stats):
    new_sputtering = Sputtering(ai_setting,screen,1,0,stats,abuse)                   
    sputterings.add(new_sputtering)
    new_sputtering = Sputtering(ai_setting,screen,-1,0,stats,abuse)                   
    sputterings.add(new_sputtering)
    new_sputtering = Sputtering(ai_setting,screen,0,1,stats,abuse)                   
    sputterings.add(new_sputtering)
    new_sputtering = Sputtering(ai_setting,screen,0,-1,stats,abuse)                   
    sputterings.add(new_sputtering)
    new_sputtering = Sputtering(ai_setting,screen,0.7,0.7,stats,abuse)                   
    sputterings.add(new_sputtering)
    new_sputtering = Sputtering(ai_setting,screen,-0.7,0.7,stats,abuse)                   
    sputterings.add(new_sputtering)
    new_sputtering = Sputtering(ai_setting,screen,0.7,-0.7,stats,abuse)                   
    sputterings.add(new_sputtering)
    new_sputtering = Sputtering(ai_setting,screen,-0.7,-0.7,stats,abuse)                   
    sputterings.add(new_sputtering)



def update_diao(ai_setting,stats,screen,ship,aliens,bullets,sb,diao,bullets_left,bullets_right):
    
    if pygame.sprite.spritecollideany(diao,bullets):
        diao_hit(ai_setting,stats,screen,ship,diao,bullets,sb)
    if pygame.sprite.spritecollideany(diao,bullets_left):
        diao_hit(ai_setting,stats,screen,ship,diao,bullets,sb)
    if pygame.sprite.spritecollideany(diao,bullets_right):
        diao_hit(ai_setting,stats,screen,ship,diao,bullets,sb)
    if pygame.Rect.colliderect(diao.rect,ship.rect):
        if stats.ship_left>0:
            stats.ship_left-=ai_setting.diao_image
            sb.prep_life()
        else:
            stats.game_active=False
            pygame.mouse.set_visible(True)


def diao_hit(ai_setting,stats,screen,ship,diao,bullets,sb):
    if ai_setting.diao_life>0:
        ai_setting.diao_life-=1
        sb.prep_diao()
        
       
      
    else:
        stats.score=4000


def diao_recover(ai_setting):
    ai_setting.recover_time+=1
    if ai_setting.recover_time==50:
        ai_setting.diao_life+=1
        ai_setting.recover_time=0




#曾的
def create_money(ai_setting,screen,stats,niao,moneyf):
    
    new_money = Money(ai_setting,screen,niao)
    moneyf.add(new_money)
def update_niao(ai_setting,screen,stats,ship,niao,sb,bullets,bullets_left,bullets_right):
    check_fleet_edges_zeng(ai_setting,screen,niao)
    niao.update()    
    niao_hit(ai_setting,stats,screen,ship,sb,niao,bullets_left,bullets_right)
    if pygame.sprite.spritecollideany(niao,bullets):
        zeng_hit(ai_setting,stats,screen,ship,niao,bullets,sb)
    if pygame.sprite.spritecollideany(niao,bullets_left):
        zeng_hit(ai_setting,stats,screen,ship,niao,bullets,sb)
    if pygame.sprite.spritecollideany(niao,bullets_right):
        zeng_hit(ai_setting,stats,screen,ship,niao,bullets,sb)
def niao_hit(ai_setting,stats,screen,ship,sb,niao,bullets_left,bullets_right):
    if pygame.Rect.colliderect(niao.rect,ship.rect):
        if stats.ship_left>0:
            stats.ship_left-=2
            sb.prep_life()
        else:
            stats.game_active=False
            pygame.mouse.set_visible(True)
def check_fleet_edges_zeng(ai_setting,screen,zeng):
    if zeng.check_edges():
        change_fleet_direction_zeng(ai_setting,screen,zeng)
def check_fleet_edges_money(ai_setting,screen,zeng,moneyf,niao):
    money = Money(ai_setting,screen,niao)
    for money in moneyf.sprites():
        if money.check_edges():
            money.speed_factor = 0
            
            
            break
def change_fleet_direction_zeng(ai_setting,screen,zeng):
    zeng.rect.x +=  ai_setting.niao_speed_factor 
    ai_setting.fleet_direction_zeng *= -1
def check_bullet_money_collisions(ai_setting,screen,stats,sb,ship,moneyf,bullets,bullets_left,bullets_right):
    collisions = pygame.sprite.groupcollide(bullets,moneyf,True,True)
    collisions = pygame.sprite.groupcollide(bullets_left,moneyf,True,True)
    collisions = pygame.sprite.groupcollide(bullets_right,moneyf,True,True)
    if collisions:
        stats.score+=ai_setting.alien_point
        sb.prep_score()
def update_moneyf(ai_setting,screen,stats,ship,zeng,moneyf,niao,sb,a,b):
    
    check_fleet_edges_money(ai_setting,screen,zeng,moneyf,niao)
    
    
    moneyf.update(a,b)

    
    if pygame.sprite.spritecollideany(ship,moneyf):
        
        moneyf_hit(ai_setting,stats,screen,ship,sb,niao,moneyf)
def moneyf_hit(ai_setting,stats,screen,ship,sb,niao,moneyf):
    if stats.ship_left>0:
        stats.ship_left-=3
        sb.prep_life()
    else:
        stats.game_active=False
        pygame.mouse.set_visible(True)
def creat_huojian_fleet(ai_setting,screen,huojians):
    """创建火箭群"""
    #创建一个火箭，并计算一行可容纳多少个火箭
    #火箭间距为火箭宽度
    huojian = Huojian(ai_setting,screen)

    number_huojians_x = get_number_aliens_x(ai_setting,huojian.rect.width)    
    huojian_width = huojian.rect.width


    #创建一行火箭

    for huojian_number in range(number_huojians_x):
        create_huojian(ai_setting,screen,huojians,huojian_number)
def get_number_huojians_x(ai_setting,huojian_width):
    available_space_x=ai_setting.screen_width - huojian_width
    number_huojians_x = int(available_space_x / (huojian_width*2))
    return number_huojians_x
def create_huojian(ai_setting,screen,huojians,huojian_number):
    huojian = Huojian(ai_setting,screen)
    huojian_width = huojian.rect.width+100
    huojian.x = huojian_width+(huojian.width*2)*huojian_number
    huojian.rect.x = huojian.x
    huojians.add(huojian)
def check_huojians_bottom(ai_setting,stats,screen,huojians):
    screen_rect=screen.get_rect()
    for huojian in huojians.sprites():
        if huojian.rect.top>=screen_rect.bottom:
            huojians.remove(huojian)
      
def update_huojians(ai_setting,stats,screen,niao,ship,huojians,sb):
    
    huojians.update()
    check_huojians_bottom(ai_setting,stats,screen,huojians)
    if pygame.sprite.spritecollideany(ship,huojians):
        
       huojians_hit(ai_setting,stats,screen,ship,sb,niao)
    if len(huojians)==0:
        creat_huojian_fleet(ai_setting,screen,huojians)
def huojians_hit(ai_setting,stats,screen,ship,sb,niao):
    if stats.ship_left>0:
        stats.ship_left-=3
        sb.prep_life()
    else:
        stats.game_active=False
        pygame.mouse.set_visible(True)
def zeng_hit(ai_setting,stats,screen,ship,niao,bullets,sb):
        if ai_setting.niao_life>0:
            ai_setting.niao_life-=1
        else:
            stats.score = 1500

#熊
def create_qzg(ai_setting,screen,stats,xiong,qzgs):
    if stats.score>1500 and len(qzgs) < ai_setting.qzg_allowed:
        new_qzg = Qzg(ai_setting,screen,xiong)
        qzgs.add(new_qzg)
def change_fleet_direction_qzg(ai_setting,screen,xiong,qzgs):
     
    ai_setting.fleet_direction_qzg*=-1
def update_xiong(ai_setting,screen,stats,ship,xiong,sb,bullets,bullets_left,bullets_right):
    check_fleet_edges_cong(ai_setting,screen,xiong)
    xiong.update()    
    xiong_hit(ai_setting,stats,screen,ship,sb,xiong)
    if pygame.sprite.spritecollideany(xiong,bullets):
        xiong_bullet_hit(ai_setting,stats,screen,bullets,sb,xiong)
    if pygame.sprite.spritecollideany(xiong,bullets_left):
        xiong_bullet_hit(ai_setting,stats,screen,bullets,sb,xiong)
    if pygame.sprite.spritecollideany(xiong,bullets_right):
        xiong_bullet_hit(ai_setting,stats,screen,bullets,sb,xiong)
def xiong_hit(ai_setting,stats,screen,ship,sb,xiong):
    if pygame.Rect.colliderect(xiong.rect,ship.rect):
        if stats.ship_left>0:
            stats.ship_left-=2
            sb.prep_life()
        else:
            stats.game_active=False
            pygame.mouse.set_visible(True)
def check_fleet_edges_cong(ai_setting,screen,cong):
    if cong.check_edges():
         change_fleet_direction_cong(ai_setting,screen,cong)
def check_fleet_edges_qzg(ai_setting,screen,qzgs,xiong):
    qzg = Qzg(ai_setting,screen,xiong)
    for qzg in qzgs.sprites():
        if qzg.check_edges():
            
            change_fleet_direction_qzg(ai_setting,screen,xiong,qzgs)
            
            break
def check_bullet_qzg_collisions(ai_setting,screen,stats,sb,ship,qzgs,bullets):
    collisions = pygame.sprite.groupcollide(bullets,qzgs,True,False)
    if collisions:
        stats.score+=ai_setting.alien_point
        sb.prep_score()
def update_qzgs(ai_setting,screen,stats,ship,qzgs,xiong,sb,bullets):
    
    check_fleet_edges_qzg(ai_setting,screen,qzgs,xiong)
    
    #create_money(ai_setting,screen,niao,moneyf)
    qzgs.update()

    
    if pygame.sprite.spritecollideany(ship,qzgs):
        
         qzgs_hit(ai_setting,stats,screen,ship,sb,xiong,qzgs)
    if pygame.sprite.groupcollide(qzgs,bullets,False,True):
         qzg_bullet_hit(ai_setting,stats,screen,bullets,sb,qzgs,xiong)
def qzgs_hit(ai_setting,stats,screen,ship,sb,xiong,qzgs):
    if stats.ship_left>0:
        stats.ship_left-=3
        sb.prep_life()
    else:
        stats.game_active=False
        pygame.mouse.set_visible(True)
def creat_hailang_fleet(ai_setting,screen,hailangs):
    """创建火箭群"""
    #创建一个火箭，并计算一行可容纳多少个火箭
    #火箭间距为火箭宽度
    hailang = Hailang(ai_setting,screen)

    number_hailangs_x = get_number_aliens_x(ai_setting,hailang.rect.width)    
    hailang_width = hailang.rect.width


    #创建一行火箭

    for hailang_number in range(number_hailangs_x):
        create_hailang(ai_setting,screen,hailangs,hailang_number)
def get_number_hailangs_x(ai_setting,hailang_width):
    available_space_x=ai_setting.screen_width - hailang_width
    number_hailangs_x = int(available_space_x / (hailang_width*2))
    return number_hailangs_x
def create_hailang(ai_setting,screen,hailangs,hailang_number):
    hailang = Hailang(ai_setting,screen)
    hailang_width = hailang.rect.width+100
    hailang.x = hailang_width+(hailang.width*2)*hailang_number
    hailang.rect.x = hailang.x
    hailangs.add(hailang)  
def check_hailangs_bottom(ai_setting,stats,screen,hailangs):
    screen_rect=screen.get_rect()
    for hailang in hailangs.sprites():
        if hailang.rect.top>=screen_rect.bottom:
            hailangs.remove(hailang)
      
def update_hailangs(ai_setting,stats,screen,xiong,ship,hailangs,sb):
    
    hailangs.update()
    check_hailangs_bottom(ai_setting,stats,screen,hailangs)
    if pygame.sprite.spritecollideany(ship,hailangs):
        
       hailangs_hit(ai_setting,stats,screen,ship,sb,xiong,hailangs)
    if len(hailangs)==0:
        creat_hailang_fleet(ai_setting,screen,hailangs)
def hailangs_hit(ai_setting,stats,screen,ship,sb,xiong,hailangs):
    if stats.ship_left>0:
        stats.ship_left-=3
        sb.prep_life()
    else:
        stats.game_active=False
        pygame.mouse.set_visible(True)
    
def xiong_bullet_hit(ai_setting,stats,screen,bullets,sb,xiong):
    if stats.xiong_left>0:
        stats.xiong_left-=1
        #sb.prep_xiong_life()
      
    else:
        stats.score=2500
def change_fleet_direction_cong(ai_setting,screen,cong):
    cong.rect.x +=  ai_setting.xiong_speed_factor 
    ai_setting.fleet_direction_cong *= -1    

def qzg_bullet_hit(ai_setting,stats,screen,bullets,sb,qzgs,xiong):
    qzg = Qzg(ai_setting,screen,xiong)
    if stats.Qzg_left>0:
        stats.Qzg_left-=1
        
      
    else:
        qzgs.remove(qzg)
        
def qzgdx(ai_setting,screen,stats,qzgs,ship,xiong,sb):
    number = 0
    qzg = Qzg(ai_setting,screen,xiong)
    for qzg in qzgs:
        number+=1
    if stats.ship_left>0:
        stats.ship_left-=1*number
        sb.prep_life()
    else:
        stats.game_active=False
        pygame.mouse.set_visible(True)
def zbly_ship_hit(ai_setting,screen,stats,zbly,ship,sb):
    if pygame.Rect.colliderect(ship.rect,zbly.rect):
        if stats.ship_left>0:
            stats.ship_left-=1
        else:
            stats.game_active=False
            pygame.mouse.set_visible(True)

