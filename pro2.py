import pygame
import random

def generate_board(filled_cells):
    board = [[0 for _ in range(9)] for _ in range(9)]

    for _ in range(filled_cells):
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        num = random.randint(1, 9)

        while not is_valid_move(board, row, col, num):
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            num = random.randint(1, 9)

        board[row][col] = num

    return board


def is_valid_move(board, row, col, num):

    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False


    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True


def draw_board(board, screen):
    cell_size = 60
    for row in range(9):
        for col in range(9):
            pygame.draw.rect(screen, (255, 255, 255), (col * cell_size, row * cell_size, cell_size, cell_size))
            if board[row][col] != 0:
                font = pygame.font.Font(None, 40)
                text = font.render(str(board[row][col]), True, (0, 0, 0))
                screen.blit(text, (col * cell_size + 20, row * cell_size + 20))


def get_cell_from_pos(pos):
    cell_size = 60
    cell_x = pos[1] // cell_size
    cell_y = pos[0] // cell_size
    return cell_x, cell_y


pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Sudoku Game")


levels = {
    "easy": 30,
    "medium": 20,
    "hard": 10,
}


level = "easy"


board = generate_board(levels[level])


draw_board(board, screen)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            cell_x, cell_y = get_cell_from_pos(pos)
            if board[cell_x][cell_y] == 0:
                board[cell_x][cell_y] = 2
                draw_board(board, screen)
    pygame.display.update()
