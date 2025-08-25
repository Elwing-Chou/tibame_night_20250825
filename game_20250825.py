import pygame as pg

pg.init()
font = pg.font.Font(None, 200)
#設定視窗
width, height = 800, 800
screen = pg.display.set_mode((width, height))
pg.display.set_caption("五子棋")

#建立畫布bg
bg = pg.Surface(screen.get_size())
bg = bg.convert()
bg.fill([199, 167, 82])

screen.blit(bg, (0,0))
pg.display.update()

# 讓遊戲不要結束
running = True
game_round = 0
while running:
    ev = pg.event.get()
    for event in ev:
        if event.type == pg.QUIT:
            running = False

pg.quit()
