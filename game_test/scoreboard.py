#!/usr/bin/env python   
# _*_ coding:utf-8 _*_
import pygame.ftfont


class Scoreboard:
    """显示得分信息的类"""
    def __init__(self, ai_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        self.text_color = (30, 30, 30)
        self.font = pygame.ftfont._SysFont(None, 48)

        self.prep_score()

    def prep_score(self):
        """将得分转化为一副渲染的图像"""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

        # 显示在右上方

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """在屏幕上显示的分"""
        self.screen.blit(self.score_image, self.screen_rect)
