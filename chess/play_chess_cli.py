import chess.game as chess
from chess.board import Chessboard


def welcome_user(first_game):
    if first_game:
        print("Welcome to Checkmate, the ultimate destination for playing chess!!\n")
    print("Would you like to play chess? y/n ")
    user_input = input("> ").lower()
    while user_input != "y" and user_input != "n":
        print('Must enter valid response: "y" or "n", try again')
        user_input = input("> ").lower()
    return user_input == "y"


def play_chess_cli():
    first_game = True
    while welcome_user(first_game):
        first_game = False
        print('Let the games begin, if at any point you want to quit, type "Forfeit"')
        game_board = Chessboard()
        game_running = True
        curr_player = "White"
        while game_running:
            print(f"{curr_player}'s turn")
            valid_move = False
            while not valid_move:
                game_board.render()
                user_input = input("Where would you like to move: ")
                if user_input.lower() == "forfeit":
                    if curr_player == "White":
                        print("Black Wins!!\n")
                    else:
                        print("White Wins!!\n")
                    game_running = False
                    break
                parsed_input = chess.parse_input(user_input)
                if not parsed_input:
                    print(
                        'Please answer in the format "B2 B3". Must be in range A-H and 1-8')
                elif not chess.validate_move(parsed_input[0], parsed_input[1], game_board, curr_player.lower(), True):
                    print('Move not possible')
                elif chess.check_check(curr_player.lower(), game_board, parsed_input):
                    print("You may not cause your own king to be put in check")
                else:
                    valid_move = True
                    chess.move_piece(parsed_input[0], parsed_input[1], game_board.board)
            if curr_player == "White" and game_running:
                if chess.check_check("black", game_board):
                    if chess.check_checkmate("black", game_board):
                        game_board.render()
                        print(f"CHECKMATE! {curr_player} wins!!\n")
                        game_running = False
                    else:
                        print("Check!")
                curr_player = "Black"
            elif curr_player == "Black" and game_running:
                if chess.check_check("white", game_board):
                    if chess.check_checkmate("white", game_board):
                        game_board.render()
                        print(f"CHECKMATE! {curr_player} wins!!\n")
                        game_running = False
                    else:
                        print("Check!")
                curr_player = "White"


if __name__ == '__main__':
    play_chess_cli()
