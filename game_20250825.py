import pygame as pg
import constants as const


def check_winner(board, board_i, board_j):
    # 橫的(往左延伸, 往右延伸, 看有幾個跟我一樣)
    sample = board[board_i][board_j]
    count = 1
    # 往右移幾個
    offset = 1
    while True:
        # 超過棋盤了
        if not (0 <= board_j + offset < len(board)):
            break
        # 沒超過棋盤, 檢查是否相等
        if board[board_i][board_j+offset] == sample:
            count = count + 1
        else:
            break
        offset = offset + 1

    offset = 1
    while True:
        # 超過棋盤了
        if not (0 <= board_j - offset < len(board)):
            break
        # 沒超過棋盤, 檢查是否相等
        if board[board_i][board_j-offset] == sample:
            count = count + 1
        else:
            break
        offset = offset + 1
    # 超過五個, 贏了
    if count >= 5:
        return True

    # 直的
    sample = board[board_i][board_j]
    count = 1
    # 往右移幾個
    offset = 1
    while True:
        # 超過棋盤了
        if not (0 <= board_i + offset < len(board)):
            break
        # 沒超過棋盤, 檢查是否相等
        if board[board_i+offset][board_j] == sample:
            count = count + 1
        else:
            break
        offset = offset + 1

    offset = 1
    while True:
        # 超過棋盤了
        if not (0 <= board_i - offset < len(board)):
            break
        # 沒超過棋盤, 檢查是否相等
        if board[board_i-offset][board_j] == sample:
            count = count + 1
        else:
            break
        offset = offset + 1
    # 超過五個, 贏了
    if count >= 5:
        return True

    # 左上->右下
    sample = board[board_i][board_j]
    count = 1
    # 往右移幾個
    offset = 1
    while True:
        # i超過棋盤了
        if not (0 <= board_i + offset < len(board)):
            break
        if not (0 <= board_j + offset < len(board)):
            break
        # 沒超過棋盤, 檢查是否相等
        if board[board_i+offset][board_j+offset] == sample:
            count = count + 1
        else:
            break
        offset = offset + 1

    offset = 1
    while True:
        # 超過棋盤了
        if not (0 <= board_i - offset < len(board)):
            break
        if not (0 <= board_j - offset < len(board)):
            break
        # 沒超過棋盤, 檢查是否相等
        if board[board_i-offset][board_j-offset] == sample:
            count = count + 1
        else:
            break
        offset = offset + 1
    # 超過五個, 贏了
    if count >= 5:
        return True

    # 右上->左下
    sample = board[board_i][board_j]
    count = 1
    # 往右移幾個
    offset = 1
    while True:
        # i超過棋盤了
        if not (0 <= board_i + offset < len(board)):
            break
        if not (0 <= board_j - offset < len(board)):
            break
        # 沒超過棋盤, 檢查是否相等
        if board[board_i+offset][board_j-offset] == sample:
            count = count + 1
        else:
            break
        offset = offset + 1

    offset = 1
    while True:
        # 超過棋盤了
        if not (0 <= board_i - offset < len(board)):
            break
        if not (0 <= board_j + offset < len(board)):
            break
        # 沒超過棋盤, 檢查是否相等
        if board[board_i-offset][board_j+offset] == sample:
            count = count + 1
        else:
            break
        offset = offset + 1
    # 超過五個, 贏了
    if count >= 5:
        return True

    return False


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

# 0830: 棋盤
board = [[const.NOT_SET] * 15 for i in range(15)]
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
            # 0830: 記得你再list裡跟你座標是反過來的
            board_i = y_line - 1
            board_j = x_line - 1
            if (1 <= x_line <= 15) and (1 <= y_line <= 15):
                # 0830: 這個位置還未落子
                if board[board_i][board_j] == const.NOT_SET:
                    # pygame.draw.circle(畫布, 顏色, (x坐標, y坐標), 半徑, 線寬)
                    if game_round % 2 == 0:
                        color = [255, 255, 255]
                        player = const.WHITE
                    else:
                        color = [0, 0, 0]
                        player = const.BLACK
                    # 0830: 沒落子的話就真的照回合落白或黑
                    board[board_i][board_j] = player
                    game_round = game_round + 1
                    pg.draw.circle(bg, color, [x_line*50, y_line*50], 25, 0)
                    screen.blit(bg, [0,0])
                    pg.display.update()
                    # 如果這步產生winner, 結束遊戲
                    if check_winner(board, board_i, board_j):
                        running = False
pg.quit()
