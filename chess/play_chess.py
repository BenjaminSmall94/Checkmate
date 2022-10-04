import pygame
import sys
import chess.game as chess
from chess.board import Chessboard

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 600

starter_board = [["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                ["{p}", "{p}", "{p}", "{p}", "{p}", "{p}", "{p}", "{p}"],
                ["x",    "x",   "x",   "x", "x",   "x",   "x",   "x"],
                ["x",    "x",   "x",   "x", "x",   "x",   "x",   "x"],
                ["x",    "x",   "x",   "x", "x",   "x",   "x",   "x"],
                ["x",    "x",   "x",   "x", "x",   "x",   "x",   "x"],
                ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]]

BOARD_SQUARE_COUNT = 8  # 8 x 8 Chessboard
BOARD_HEIGHT = 480
BOARD_WIDTH = 480
GRID_WIDTH = BOARD_HEIGHT / BOARD_SQUARE_COUNT
GRID_HEIGHT = BOARD_WIDTH / BOARD_SQUARE_COUNT


def draw_grid(surface):
    for row in range(0, BOARD_SQUARE_COUNT):
        for col in range(0, BOARD_SQUARE_COUNT):
            if (row + col) % 2 == 0:
                r = pygame.Rect((col*GRID_WIDTH, row*GRID_HEIGHT), (GRID_WIDTH, GRID_HEIGHT))
                pygame.draw.rect(surface, (155, 155, 155), r)
            else:
                r = pygame.Rect((col*GRID_WIDTH, row*GRID_HEIGHT), (GRID_WIDTH, GRID_HEIGHT))
                pygame.draw.rect(surface, (255, 255, 255), r)
        r1 = pygame.Rect((0, BOARD_HEIGHT + 2), (SCREEN_WIDTH, 118))
        pygame.draw.rect(surface, (255, 255, 255), r1)
        r2 = pygame.Rect((310, 514), (80, 40))
        pygame.draw.rect(surface, (0, 0, 0), r2, 2)


def handle_mouse():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            return pos


def blit_pieces(screen, images, board):
    for row_idx, row in enumerate(board.board):
        for col_idx, col_val in enumerate(row):
            if len(col_val) > 1:
                if col_val[0] == '[':
                    if col_val[1] == "K":
                        screen.blit(images["white-king"], (col_idx * GRID_WIDTH, row_idx * GRID_HEIGHT))
                    elif col_val[1] == "Q":
                        screen.blit(images["white-queen"], (col_idx * GRID_WIDTH, row_idx * GRID_HEIGHT))
                    elif col_val[1] == "r":
                        screen.blit(images["white-rook"], (col_idx * GRID_WIDTH, row_idx * GRID_HEIGHT))
                    elif col_val[1] == "b":
                        screen.blit(images["white-bishop"], (col_idx * GRID_WIDTH, row_idx * GRID_HEIGHT))
                    elif col_val[1] == "k":
                        screen.blit(images["white-knight"], (col_idx * GRID_WIDTH, row_idx * GRID_HEIGHT))
                    else:
                        screen.blit(images["white-pawn"], (col_idx * GRID_WIDTH, row_idx * GRID_HEIGHT))
                else:
                    if col_val[1] == "K":
                        screen.blit(images["black-king"], (col_idx * GRID_WIDTH, row_idx * GRID_HEIGHT))
                    elif col_val[1] == "Q":
                        screen.blit(images["black-queen"], (col_idx * GRID_WIDTH, row_idx * GRID_HEIGHT))
                    elif col_val[1] == "r":
                        screen.blit(images["black-rook"], (col_idx * GRID_WIDTH, row_idx * GRID_HEIGHT))
                    elif col_val[1] == "b":
                        screen.blit(images["black-bishop"], (col_idx * GRID_WIDTH, row_idx * GRID_HEIGHT))
                    elif col_val[1] == "k":
                        screen.blit(images["black-knight"], (col_idx * GRID_WIDTH, row_idx * GRID_HEIGHT))
                    else:
                        screen.blit(images["black-pawn"], (col_idx * GRID_WIDTH, row_idx * GRID_HEIGHT))


def setup_UI():
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    draw_grid(surface)
    images = {
        "white-king": pygame.image.load("chess/icons/white-king.png"),
        "white-queen": pygame.image.load("chess/icons/white-queen.png"),
        "white-rook": pygame.image.load("chess/icons/white-rook.png"),
        "white-bishop": pygame.image.load("chess/icons/white-bishop.png"),
        "white-knight": pygame.image.load("chess/icons/white-knight.png"),
        "white-pawn": pygame.image.load("chess/icons/white-pawn.png"),
        "black-king": pygame.image.load("chess/icons/black-king.png"),
        "black-queen": pygame.image.load("chess/icons/black-queen.png"),
        "black-rook": pygame.image.load("chess/icons/black-rook.png"),
        "black-bishop": pygame.image.load("chess/icons/black-bishop.png"),
        "black-knight": pygame.image.load("chess/icons/black-knight.png"),
        "black-pawn": pygame.image.load("chess/icons/black-pawn.png"),
    }
    LETTER_FONT = pygame.font.SysFont('comicsans', 20)
    return clock, screen, surface, images, LETTER_FONT


def play_chess():
    pygame.init()
    clock, screen, surface, images, LETTER_FONT = setup_UI()

    game_board = Chessboard()
    game_running = True
    curr_player = "White"
    start_space = None
    while True:
        clock.tick(10)
        clicked_coordinates = handle_mouse()
        if clicked_coordinates:
            if clicked_coordinates[1] <= 480 and game_running:
                if start_space:
                    end_space = int(clicked_coordinates[0] // GRID_WIDTH), int(clicked_coordinates[1] // GRID_HEIGHT)
                    start_pos_text = f"{chr(start_space[0] + 65)}{8 - start_space[1]}"
                    end_pos_text = f"{chr(end_space[0] + 65)}{8 - end_space[1]}"
                    if not chess.validate_move(start_pos_text, end_pos_text, game_board, curr_player.lower(), True):
                        print("Invalid Move")
                    elif chess.check_check(curr_player.lower(), game_board, (start_pos_text, end_pos_text)):
                        print("You may not cause your king to move into check or allow him to remain in check")
                    else:
                        chess.move_piece(start_pos_text, end_pos_text, game_board.board)
                        if curr_player == "White" and game_running:
                            if chess.check_check("black", game_board):
                                if chess.check_checkmate("black", game_board):
                                    print(f"CHECKMATE! {curr_player} wins!!\n")
                                    game_running = False
                                    draw_grid(surface)
                                    continue
                                else:
                                    print("Check!")
                            curr_player = "Black"
                        elif curr_player == "Black" and game_running:
                            if chess.check_check("white", game_board):
                                if chess.check_checkmate("white", game_board):
                                    print(f"CHECKMATE! {curr_player} wins!!\n")
                                    game_running = False
                                    draw_grid(surface)
                                    continue
                                else:
                                    print("Check!")
                            curr_player = "White"
                    start_space = None
                    draw_grid(surface)
                else:
                    start_space = int(clicked_coordinates[0] // GRID_WIDTH), int(clicked_coordinates[1] // GRID_HEIGHT)
                    r = pygame.Rect((start_space[0] * GRID_WIDTH, start_space[1] * GRID_HEIGHT), (GRID_WIDTH, GRID_HEIGHT))
                    pygame.draw.rect(surface, (255, 0, 0), r, 3)
            else:
                if 514 <= clicked_coordinates[1] <= 554 and 310 <= clicked_coordinates[0] <= 390:
                    print("Reset")
                    game_board = Chessboard()
                    curr_player = "White"
                    start_space = None
                    game_running = True
                    draw_grid(surface)
        if game_running:
            message_text = f"{curr_player}'s Turn"
        else:
            message_text = f"{curr_player} Wins!!"
        pytext = LETTER_FONT.render(message_text, 1, (0, 0, 0))
        reset = "Reset"
        res_text = LETTER_FONT.render(reset, 1, (0, 0, 0))
        screen.blit(surface, (0, 0))
        blit_pieces(screen, images, game_board)
        screen.blit(pytext, (75, 518))
        screen.blit(res_text, (320, 518))
        pygame.display.update()


if __name__ == '__main__':
    play_chess()
