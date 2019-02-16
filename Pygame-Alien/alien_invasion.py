import pygame
from pygame.sprite import Group  # 导入Group类
from settings import Settings  # 导入settings类
from ship import Ship
import game_functions as gf


def run_game():
    pygame.init()
    ai_settings = Settings()  # 生成settings的实例
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))  # 生成surface对象
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_aliens(aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
