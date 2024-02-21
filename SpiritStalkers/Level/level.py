import pygame
import sys

from SpiritStalkers.Button.button import Button
from SpiritStalkers.Text.texts import Text

# 初始化pygame
pygame.init()
screen_size = (800, 600)
WIDTH, HEIGHT = 640, 384
title_font = "Fonts/Aladin-Regular.ttf"
instructions_font = 'Fonts/BubblegumSans-Regular.ttf'
win = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)
# 设置窗口大小
screen = pygame.display.set_mode((800, 600))
background = pygame.image.load('assets/BG1.png')
# 如果需要，可以调整背景图片大小以适应窗口
background = pygame.transform.scale(background, screen_size)
# 设置颜色
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# 关卡区域（示例）
levels = [pygame.Rect(100, 100, 100, 50), pygame.Rect(300, 100, 100, 50)]
BG1 = pygame.transform.scale(pygame.image.load('assets/BG1.png'), (WIDTH, HEIGHT))
BG2 = pygame.transform.scale(pygame.image.load('assets/BG2.png'), (WIDTH, HEIGHT))
BG3 = pygame.transform.scale(pygame.image.load('assets/BG3.png'), (WIDTH, HEIGHT))
MOON = pygame.transform.scale(pygame.image.load('assets/moon.png'), (300, 220))


# 设置声音
diamond_fx = pygame.mixer.Sound('sounds/point.mp3')
diamond_fx.set_volume(0.6)

# 设置文字
t = Text(instructions_font, 18)
font_color = (12, 12, 12)
Level1 = t.render('Level-1', font_color)
Level2 = t.render('Level-2', font_color)
Level3 = t.render('Level-3', font_color)
Level4 = t.render('Level-4', font_color)
main_menu = t.render('Main Menu', font_color)
# 设置按钮
ButtonBG = pygame.image.load('assets/ButtonBG.png')
bwidth = ButtonBG.get_width()
level_buttons = [
    Button(170, 120, ButtonBG, 0.5, Level1, 10),
    Button(320, 120, ButtonBG, 0.5, Level2, 10),
    Button(170, 200, ButtonBG, 0.5, Level3, 10),
    Button(320, 200, ButtonBG, 0.5, Level4, 10)


]
Level1_btn = Button(WIDTH // 2 - bwidth // 4, HEIGHT // 2, ButtonBG, 0.5, Level1, 10)
level2_btn = Button(WIDTH // 2 - bwidth // 4, HEIGHT // 2 + 30, ButtonBG, 0.5, Level2, 10)
main_menu_btn = Button(WIDTH // 2 - bwidth // 4, HEIGHT // 2 + 150, ButtonBG, 0.5, main_menu, 20)
bg_scroll = 0

def Level_Background(win):
    global main_menu, level_buttons, diamond_fx, background

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # 检查是否点击了关卡按钮
                for index, button in enumerate(level_buttons):
                    if button.rect.collidepoint(event.pos):
                        # 播放点击声音
                        diamond_fx.play()
                        # 点击了关卡，可以在这里运行对应关卡的游戏逻辑
                        print(f"进入第 {index + 1} 关")
                        return index + 1  # 停止检查其他按钮，因为已经找到点击的按钮
                if main_menu_btn.rect.collidepoint(event.pos):
                    diamond_fx.play()
                    return 'main_menu'  # 玩家点击了返回主菜单的按钮
        win.fill((0, 0, 0))
        # win.blit(MOON, (0, 150))
        # win.blit(background, (0, 0))
        for x in range(5):
            win.blit(BG1, ((x * WIDTH) - bg_scroll * 0.6, 0))
            win.blit(BG2, ((x * WIDTH) - bg_scroll * 0.7, 0))
            win.blit(BG3, ((x * WIDTH) - bg_scroll * 0.8, 0))
        # 绘制关卡按钮
        for button in level_buttons:
            button.draw(win)
        pygame.draw.rect(win, (255, 255, 255), (0, 0, WIDTH, HEIGHT), 4, border_radius=10)
        main_menu_btn.draw(win)
        pygame.display.flip()
