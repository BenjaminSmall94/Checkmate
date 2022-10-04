import re
import copy


def move_piece(start_pos, end_pos, board, real_move=True):
    start_pos = (7 - (int(start_pos[1]) - 1), ord(start_pos[0]) - 65)
    end_pos = (7 - (int(end_pos[1]) - 1), ord(end_pos[0]) - 65)
    moving_piece = board[start_pos[0]][start_pos[1]]
    moving_piece_color = None
    if moving_piece[0] == "[":
        moving_piece_color = True  # True == "white"
    elif moving_piece[0] == "{":
        moving_piece_color = False  # False == "black"
    board[start_pos[0]][start_pos[1]] = "x"
    board[end_pos[0]][end_pos[1]] = moving_piece
    if real_move:
        if moving_piece[1] == "p":
            if moving_piece_color and end_pos[0] == 0:
                pawn_promotion(end_pos[1], board, moving_piece_color)
            if not moving_piece_color and end_pos[0] == 7:
                pawn_promotion(end_pos[1], board, moving_piece_color)


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


def check_check(color, board, move=None):
    search_board = board
    if move:
        search_board = copy.deepcopy(board)
        move_piece(move[0], move[1], search_board.board, False)
    king_loc = find_king(color, search_board)
    for row_idx, row in enumerate(search_board.board):
        for col_idx, col_val in enumerate(row):
            if color == "white" and col_val[0] == "{":
                start_pos_text = f"{chr(col_idx + 65)}{8 - row_idx}"
                end_pos_text = f"{chr(king_loc[1] + 65)}{8 - king_loc[0]}"
                if validate_move(start_pos_text, end_pos_text, search_board, "black"):
                    return True
            elif color == "black" and col_val[0] == "[":
                start_pos_text = f"{chr(col_idx + 65)}{8 - row_idx}"
                end_pos_text = f"{chr(king_loc[1] + 65)}{8 - king_loc[0]}"
                if validate_move(start_pos_text, end_pos_text, search_board, "white"):
                    return True
    return False


def check_checkmate(color, board):
    for row_idx, row in enumerate(board.board):
        for col_idx, col_val in enumerate(row):
            if color == "white" and col_val[0] == "[":
                if can_stop_checkmate(color, board, row_idx, col_idx):
                    return False
            elif color == "black" and col_val[0] == "{":
                if can_stop_checkmate(color, board, row_idx, col_idx):
                    return False
    return True


def can_stop_checkmate(color, board, row_idx, col_idx):
    for move_row_idx, move_row in enumerate(board.board):
        for move_col_idx, move_col_val in enumerate(move_row):
            start_pos_text = f"{chr(col_idx + 65)}{8 - row_idx}"
            end_pos_text = f"{chr(move_col_idx + 65)}{8 - move_row_idx}"
            if validate_move(start_pos_text, end_pos_text, board, color):
                if not check_check(color, board, (start_pos_text, end_pos_text)):
                    return True
    return False


def find_king(color, copied_board):
    for row_idx, row in enumerate(copied_board.board):
        for col_idx, col_val in enumerate(row):
            if color == "white":
                if col_val == "[K]":
                    return row_idx, col_idx
            else:
                if col_val == "{K}":
                    return row_idx, col_idx


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


def validate_move(start_pos, end_pos, board, player_color, provide_feedback=False):
    # turn string input into array coordinates
    start_list = list(start_pos)
    end_list = list(end_pos)
    start_coord = [ord(start_list[0]) - 65, 7 - (int(start_list[1])-1)]
    end_coord = [ord(end_list[0]) - 65, 7 - (int(end_list[1])-1)]

    def get_piece(coord):
        return board.board[coord[1]][coord[0]]

    # validate piece color is same as player color
    def get_color(coord):
        # get color of piece at start_pos
        if board.board[coord[1]][coord[0]][0] == "{":
            return "black"
        if board.board[coord[1]][coord[0]][0] == "[":
            return "white"

    def check_color_match(player, piece):
        if player == piece:
            return True
        else:
            return False

    # Get the piece being moved
    piece = get_piece(start_coord)

    # Check if selected space actually has a piece
    if piece == "x":
        if provide_feedback:
            print("piece can't be empty")
        return False

    # Get color of piece being moved
    piece_color = get_color(start_coord)

    # Check if player is moving their own piece
    if not check_color_match(player_color, piece_color):
        if provide_feedback:
            print("color doesn't match")
        return False

    # make sure you can't take your own piece
    if get_color(end_coord) == player_color:
        if provide_feedback:
            print("Don't attack your own piece!")
        return False

    def validate_pawn(color, start, end, board):
        # Different direction allowed for different color
        if color == "black":
            # piece moves one space down
            if start[1] - end[1] == -1:
                # check diagonal attack
                if abs(start[0] - end[0]) == 1:
                    # check for enemy at end point
                    if board.board[end[1]][end[0]] == "x":
                        if provide_feedback:
                            print("pawn can only move diagonal if attacking")
                        return False
                    return True

            # if not attacking, pawn must stay in same column
            if start[0] != end[0]:
                return False

            # check if moving 2 spaces from home row
            if start[1] - end[1] == -2:
                if board.board[end[1]][end[0]] != "x":
                    if provide_feedback:
                        print("pawn can only move forward if empty")
                    return False
                return start[1] == 1

            # moves straight down
            if start[1] - end[1] == -1:
                # check if end point is empty
                if board.board[end[1]][end[0]] != "x":
                    if provide_feedback:
                        print("pawn can only move forward if empty")
                    return False
                return True
            return False

        if color == "white":
            # piece moves one space down
            if start[1] - end[1] == 1:
                # check diagonal attack
                if abs(start[0] - end[0]) == 1:
                    # check for enemy at end point
                    if board.board[end[1]][end[0]] == "x":
                        if provide_feedback:
                            print("pawn can only move diagonal if attacking")
                        return False
                    return True

            # if not attacking, pawn must stay in same column
            if start[0] != end[0]:
                return False

            # check if moving 2 spaces from home row
            if start[1] - end[1] == 2:
                if board.board[end[1]][end[0]] != "x":
                    if provide_feedback:
                        print("pawn can only move forward if empty")
                    return False
                return start[1] == 6

            # moves straight down
            if start[1] - end[1] == 1:
                # check if end point is empty
                if board.board[end[1]][end[0]] != "x":
                    if provide_feedback:
                        print("pawn can only move forward if empty")
                    return False
                return True
            return False

    def validate_rook(start, end, board):
        # same column
        if start[0] == end[0]:
            spaces = abs(start[1] - end[1]) - 1
            # check if moving down
            if start[1] - end[1] < 0:
                row = start[1] + 1
                col = start[0]
                while spaces > 0:
                    if board.board[row][col] != "x":
                        return False
                    row += 1
                    spaces -= 1
                return True
            # moving up
            row = start[1] - 1
            col = start[0]
            while spaces > 0:
                if board.board[row][col] != "x":
                    return False
                row -= 1
                spaces -= 1
            return True

        # same row
        if start[1] == end[1]:
            spaces = abs(start[0] - end[0]) - 1
            # check if moving right
            if start[0] - end[0] < 0:
                row = start[1]
                col = start[0] + 1
                while spaces > 0:
                    if board.board[row][col] != "x":
                        return False
                    col += 1
                    spaces -= 1
                return True
            # moving left
            row = start[1]
            col = start[0] - 1
            while spaces > 0:
                if board.board[row][col] != "x":
                    return False
                col -= 1
                spaces -= 1
            return True

        return False

    def validate_king(start, end):
        # check vertical first
        if abs(start[1] - end[1]) == 1:
            # check horizontal
            if abs(start[0] - end[0]) <= 1:
                return True

        # check horizontal first
        if abs(start[0] - end[0]) == 1:
            # check vertical
            if abs(start[1] - end[1]) <= 1:
                return True

        return False

    def validate_queen(start, end, board):
        if validate_rook(start, end, board) or validate_bishop(start, end, board):
            return True

        return False

    def validate_bishop(start, end, board):
        # check if diagonal
        if abs(start[0] - end[0]) != abs(start[1] - end[1]):
            return False

        spaces = abs(start[0] - end[0]) - 1
        # check if moving right
        if start[0] - end[0] < 0:
            # check if moving down
            if start[1] - end[1] < 0:
                row = start[1] + 1
                col = start[0] + 1
                while spaces > 0:
                    if board.board[row][col] != "x":
                        return False
                    col += 1
                    row += 1
                    spaces -= 1
                return True
            # moving up
            else:
                row = start[1] - 1
                col = start[0] + 1
                while spaces > 0:
                    if board.board[row][col] != "x":
                        return False
                    col += 1
                    row -= 1
                    spaces -= 1
                return True

        # moving left
        else:
            # check if moving down
            if start[1] - end[1] < 0:
                row = start[1] + 1
                col = start[0] - 1
                while spaces > 0:
                    if board.board[row][col] != "x":
                        return False
                    col -= 1
                    row += 1
                    spaces -= 1
                return True
            # moving up
            else:
                row = start[1] - 1
                col = start[0] - 1
                while spaces > 0:
                    if board.board[row][col] != "x":
                        return False
                    col -= 1
                    row -= 1
                    spaces -= 1
                return True

    def validate_knight(start, end):
        # check horizontal change
        if abs(start[0] - end[0]) == 2:
            # check vertical change
            if abs(start[1] - end[1]) == 1:
                return True

        # check vertical change
        if abs(start[1] - end[1]) == 2:
            # check horizontal change
            if abs(start[0] - end[0]) == 1:
                return True

        return False

    if piece[1] == "Q":
        return validate_queen(start_coord, end_coord, board)
    elif piece[1] == "r":
        return validate_rook(start_coord, end_coord, board)
    elif piece[1] == "K":
        return validate_king(start_coord, end_coord)
    elif piece[1] == "b":
        return validate_bishop(start_coord, end_coord, board)
    elif piece[1] == "k":
        return validate_knight(start_coord, end_coord)
    elif piece[1] == "p":
        return validate_pawn(piece_color, start_coord, end_coord, board)


def reset(board):
    board.__init__()
