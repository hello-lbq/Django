#!/usr/bin/env python   
# _*_ coding:utf-8 _*_
import pygame

from settings import Settings
from ship import Ship
from aline import Alien
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption(" Alien Invasion")

    # 创建一个用于储存游戏统计信息的实例
    stats = GameStats(ai_settings)
    # 创建一座飞船 储存子弹的编组  外星人编组
    # 创建一座飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于储存子弹的编组
    bullets = Group()

    # 创建外星人编组
    aliens = Group()
    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.updata()
        gf.updata_bullets(ai_settings, screen, ship, aliens, bullets)
        gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
run_game()
