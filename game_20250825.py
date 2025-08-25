import pygame as pg

pg.init()
font = pg.font.Font(None, 200)
#設定視窗
width, height = 800, 800
screen = pg.display.set_mode([width, height])
pg.display.set_caption("五子棋")

#建立畫布bg
bg = pg.Surface(screen.get_size())
bg = bg.convert()
# 填滿某個顏色(RGB) rgb都是0-255來代表強度
bg.fill([199, 167, 82])

# pygame.draw.line(畫布, 顏色, (x坐標1, y坐標1), (x坐標2, y坐標2), 線寬)
for i in range(15):
    pg.draw.line(bg, [100, 100, 100], [50*i+50, 50], [50*i+50, 750], 2)
for i in range(15):
    pg.draw.line(bg, [100, 100, 100], [50, 50*i+50], [750, 50*i+50], 2)

# blit: 把圖層真正放上去
screen.blit(bg, [0,0])
pg.display.update()

# 讓遊戲不要結束
running = True
game_round = 0
while running:
    # 接受任何的鍵盤滑鼠事件
    ev = pg.event.get()
    for event in ev:
        # 按右上角的xx
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONUP:
            x, y = pg.mouse.get_pos()
            x_line = round(x / 50.0)
            y_line = round(y / 50.0)
            if (1 <= x_line <= 15) and (1 <= y_line <= 15):
                # pygame.draw.circle(畫布, 顏色, (x坐標, y坐標), 半徑, 線寬)
                if game_round % 2 == 0:
                    color = [255, 255, 255]
                else:
                    color = [0, 0, 0]
                game_round = game_round + 1
                pg.draw.circle(bg, color, [x_line*50, y_line*50], 25, 0)
                screen.blit(bg, [0,0])
                pg.display.update()
pg.quit()
