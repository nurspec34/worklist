import random
import os

def initialize_board():
    # 初始化4x4的遊戲板，並在其中隨機生成兩個數字2或4
    board = [[0] * 4 for _ in range(4)]
    add_new_tile(board)
    add_new_tile(board)
    return board

def add_new_tile(board):
    # 在空白的位置隨機生成一個數字2或4
    empty_cells = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        board[i][j] = random.choice([2, 4])

def print_board(board):
    # 印出遊戲板的當前狀態
    os.system('clear' if os.name == 'posix' else 'cls')  # 清空螢幕
    for row in board:
        print(' '.join(str(cell) if cell != 0 else '.' for cell in row))
    print()

def slide(board, direction):
    # 將數字滑動到指定方向
    for row in board:
        row = slide_row(row, direction)

def slide_row(row, direction):
    # 將一行數字滑動到指定方向
    row = [cell for cell in row if cell != 0]
    if direction == 'left':
        row = merge(row)
        return row + [0] * (4 - len(row))
    elif direction == 'right':
        row = merge(row[::-1])
        return [0] * (4 - len(row)) + row[::-1]
    elif direction == 'up':
        row = merge(row)
        return [row[i] if i < len(row) else 0 for i in range(4)]
    elif direction == 'down':
        row = merge(row[::-1])
        return [0] * (4 - len(row)) + row[::-1]

def merge(row):
    # 合併相同數字
    for i in range(len(row) - 1):
        if row[i] == row[i + 1]:
            row[i] *= 2
            row[i + 1] = 0
    return [cell for cell in row if cell != 0]

def is_game_over(board):
    # 檢查遊戲是否結束（不能再移動）
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0 or (j < 3 and board[i][j] == board[i][j + 1]) or \
               (i < 3 and board[i][j] == board[i + 1][j]):
                return False
    return True

def main():
    board = initialize_board()
    while True:
        print_board(board)
        if is_game_over(board):
            print("遊戲結束！")
            break
        direction = input("請輸入移動方向 (上:w, 下:s, 左:a, 右:d): ").lower()
        if direction in ['w', 's', 'a', 'd']:
            slide(board, 'up' if direction == 'w' else 'down' if direction == 's' else
                  'left' if direction == 'a' else 'right')
            add_new_tile(board)
        else:
            print("輸入無效，請輸入 'w', 's', 'a' 或 'd'。")

if __name__ == "__main__":
    main(w)