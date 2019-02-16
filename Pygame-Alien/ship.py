import pygame


class Ship ():
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings
        self.image=pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()   # left、right、top、bottom
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx  # 飞船的X轴中心为屏幕的X轴中心
        self.rect.bottom = self.screen_rect.bottom
        self.centerx = float(self.rect.centerx)  # 转化为浮点型
        self.bottom = float(self.rect.bottom)    # 转化为浮点型
        # 飞船的默认状态静止
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.fire = False

    def update(self):  # 更新状态
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.centerx -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.bottom > self.rect.height:
            self.bottom -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.bottom += self.ai_settings.ship_speed_factor
        self.rect.centerx = self.centerx
        self.rect.bottom = self.bottom

    def blitme(self):  # 绘图
        self.screen.blit(self.image, self.rect)
