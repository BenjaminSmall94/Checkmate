from board import Chessboard
import re


def welcome_user():
    print("Welcome to Checkmate, the ultimate destination for playing chess!")
    print("Would you like to play chess? y/n ")
    user_input = input("> ").lower()
    while user_input != "y" and user_input != "n":
        print('Must enter valid response: "y" or "n", try again')
        input("> ")
    return user_input == "y"


def move_piece(start_pos, end_pos, board):
    start_row = 7 - (int(start_pos[1]) - 1)
    start_col = ord(start_pos[0]) - 65
    end_row = 7 - (int(end_pos[1]) - 1)
    end_col = ord(end_pos[0]) - 65
    moving_piece = board[start_row][start_col]
    moving_piece_color = None
    if moving_piece[0] == "[":
        moving_piece_color = True  # True == "white"
    elif moving_piece[0] == "{":
        moving_piece_color = False  # False == "black"
    board[start_row][start_col] = "x"
    board[end_row][end_col] = moving_piece
    if moving_piece[1] == "p":
        if moving_piece_color and end_row == 0:
            pawn_promotion(end_col, board, moving_piece_color)
        if not moving_piece_color and end_row == 7:
            pawn_promotion(end_col, board, moving_piece_color)


def parse_input(user_input):
    """
    Checks to see if user_input valid within confines of chess space and desired format, then return tuple with start_pos
    and end_pos. Returns False if invalid user_input.

    :param user_input: format "D2 D3"
    :return: tuple(D2, D3)
    """
    split_input = user_input.upper().split()
    if len(split_input) != 2:
        return False
    if split_input[0] == split_input[1]:
        return False
    for pos in split_input:
        pattern = r"^[A-H][1-8]$"
        if not re.match(pattern, pos):
            return False
    return tuple(split_input)


def validate_move(piece, start_pos, end_pos, board):

    def validate_pawn(color, start_pos, end_pos, board):
        pass

    def validate_rook(start_pos, end_pos, board):
        pass

    def validate_king(start_pos, end_pos, board):
        pass

    def validate_queen(start_pos, end_pos, board):
        pass

    def validate_bishop(start_pos, end_pos, board):
        pass

    def validate_knight(start_pos, end_pos, board):
        pass

    if piece[1] == "Q":
        return validate_queen(start_pos, end_pos, board)
    elif piece[1] == "r":
        return validate_rook(start_pos, end_pos, board)
    elif piece[1] == "K":
        return validate_king(start_pos, end_pos, board)
    elif piece[1] == "b":
        return validate_bishop(start_pos, end_pos, board)
    elif piece[1] == "k":
        return validate_knight(start_pos, end_pos, board)
    elif piece == "{p}":
        return validate_pawn("black", start_pos, end_pos, board)
    elif piece == "[p]":
        return validate_pawn("white", start_pos, end_pos, board)


def check_check(color, board):
    pass


def check_checkmate(color, board):
    pass


def pawn_promotion(end_col, board, curr_color):
    print('PAWN PROMOTION: What piece would you like to promote to? ("Q", "r", "b", "k")')
    promotion_type = input("> ")
    while promotion_type != "Q" and promotion_type != "r" and promotion_type != "b" and promotion_type != "k":
        print('Please enter valid input ("Q", "r", "b", "k")')
        promotion_type = input("> ")
    if curr_color:
        board[0][end_col] = f"[{promotion_type}]"
    else:
        board[7][end_col] = f"{{{promotion_type}}}"


def reset(board):
    board.__init__()


def play_game():
    if welcome_user():
        game_board = Chessboard()
        curr_player = "White"
        while True:
            game_board.render()
            print(f"{curr_player}'s turn")
            valid_move = False
            while not valid_move:
                user_input = input("Where would you like to move: ")
                valid_parsed_input = parse_input(user_input)
                if not valid_parsed_input:
                    print('Please answer in the format "B2 B3". Must be in range A-H and 1-8')
                    continue
                # if validate_move(valid_parsed_input[0], valid_parsed_input[1], game_board, curr_player.lower):
                #     valid_move = valid_parsed_input
                valid_move = valid_parsed_input  # placeholder until validate move is functional
            move_piece(valid_move[0], valid_move[1], game_board.board)
            if curr_player == "White":
                curr_player = "Black"
            elif curr_player == "Black":
                curr_player = "White"


play_game()
