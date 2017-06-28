#!/usr/bin/env python   
# _*_ coding:utf-8 _*_


class Settings:
    """ 存储《外星人入侵》的所有设置的类 """

    def __init__(self):
        """初始化游戏设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # 飞船的设置
        self.ship_speed_factor = 1.5
        self.ship_limit = 3
        # 子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 10
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 5

        # 外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 50
        # fleet_direction为1 表示向右移， -1为向左移
        self.fleet_direction = 1
