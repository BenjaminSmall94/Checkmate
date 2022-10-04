import pytest
import chess.game as c
import chess.board as b


# @pytest.mark.skip("pending")
def test_validate_move_white_pawn_one():
    board = b.Chessboard()
    actual = c.validate_move("A2", "A3", board, "white")
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_white_pawn_two():
    board = b.Chessboard()
    actual = c.validate_move("A2", "A4", board, "white")
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_white_pawn_one_blocked():
    board = b.Chessboard([["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                          ["{p}", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[Q]", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("A2", "A3", board, "white")
    expected = False
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_white_pawn_two_blocked():
    board = b.Chessboard([["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                          ["{p}", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[Q]", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("A2", "A4", board, "white")
    expected = False
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_black_pawn_one():
    board = b.Chessboard()
    actual = c.validate_move("A7", "A6", board, "black")
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_black_pawn_two():
    board = b.Chessboard()
    actual = c.validate_move("A7", "A5", board, "black")
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_black_pawn_one_blocked():
    board = b.Chessboard([["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                          ["{p}", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["[Q]", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("A7", "A6", board, "black")
    expected = False
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_black_pawn_two_blocked():
    board = b.Chessboard([["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                          ["{p}", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[Q]", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("A7", "A5", board, "black")
    expected = False
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_white_pawn_two_not_home():
    board = b.Chessboard([["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                          ["{p}", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("A3", "A5", board, "white")
    expected = False
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_black_pawn_two_not_home():
    board = b.Chessboard([["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                          ["x", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["{p}", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("A6", "A4", board, "black")
    expected = False
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_white_pawn_diagonal():
    board = b.Chessboard()
    actual = c.validate_move("A2", "B3", board, "white")
    expected = False
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_black_pawn_diagonal():
    board = b.Chessboard()
    actual = c.validate_move("A7", "B6", board, "black")
    expected = False
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_white_pawn_diagonal_attack():
    board = b.Chessboard([["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                          ["x", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "{p}", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("A2", "B3", board, "white")
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_black_pawn_diagonal_attack():
    board = b.Chessboard([["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                          ["{p}", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "[p]", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("A7", "B6", board, "black")
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_white_pawn_backward():
    board = b.Chessboard([["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                          ["{p}", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "[p]", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "x", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("B4", "B3", board, "white")
    expected = False
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_black_pawn_backward():
    board = b.Chessboard([["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                          ["{p}", "x", "{p}", "{p}", "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "{p}", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("B5", "B6", board, "black")
    expected = False
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_white_pawn_sideways():
    board = b.Chessboard([["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                          ["{p}", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "[p]", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "x", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("B4", "C4", board, "white")
    expected = False
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_black_pawn_sideways():
    board = b.Chessboard([["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                          ["{p}", "x", "{p}", "{p}", "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "{p}", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("B5", "C5", board, "black")
    expected = False
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_white_rook_forward():
    board = b.Chessboard([["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                          ["{p}", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("A1", "A5", board, "white")
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_black_rook_forward():
    board = b.Chessboard([["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                          ["x", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("A8", "A4", board, "black")
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_white_rook_backward():
    board = b.Chessboard([["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                          ["{p}", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[r]", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["x", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("A5", "A1", board, "white")
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_black_rook_backward():
    board = b.Chessboard([["x", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                          ["x", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["{r}", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("A4", "A8", board, "black")
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_white_rook_sideways():
    board = b.Chessboard([["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                          ["{p}", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[r]", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["x", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("A5", "F5", board, "white")
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_black_rook_sideways():
    board = b.Chessboard([["x", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                          ["x", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["{r}", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("A4", "F4", board, "black")
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_white_rook_forward_blocked():
    board = b.Chessboard()
    actual = c.validate_move("A1", "A5", board, "white")
    expected = False
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_black_rook_forward_blocked():
    board = b.Chessboard()
    actual = c.validate_move("A8", "A4", board, "black")
    expected = False
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_white_rook_sideways_blocked():
    board = b.Chessboard()
    actual = c.validate_move("A1", "F1", board, "white")
    expected = False
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_black_rook_sideways_blocked():
    board = b.Chessboard()
    actual = c.validate_move("A8", "F8", board, "black")
    expected = False
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_white_rook_forward_attack():
    board = b.Chessboard([["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                          ["x", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["{p}", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("A1", "A5", board, "white")
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_black_rook_forward_attack():
    board = b.Chessboard([["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                          ["x", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("A8", "A4", board, "black")
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_white_rook_sideways_attack():
    board = b.Chessboard([["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                          ["{p}", "{p}", "x", "{p}", "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[r]", "x", "{p}", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["x", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("A5", "C5", board, "white")
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_black_rook_sideways_attack():
    board = b.Chessboard([["x", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                          ["x", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["{r}", "x", "[p]", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "x", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("A4", "C4", board, "black")
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_white_rook_diagonal():
    board = b.Chessboard([["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                          ["{p}", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[r]", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["x", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("A5", "B4", board, "white")
    expected = False
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_black_rook_diagonal():
    board = b.Chessboard([["x", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                          ["x", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["{r}", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("A4", "B5", board, "black")
    expected = False
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_white_king_forward():
    board = b.Chessboard([["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                          ["{p}", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "[K]", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "x", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("E4", "E5", board, "white")
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_black_king_forward():
    board = b.Chessboard([["x", "{k}", "{b}", "{Q}", "x", "{b}", "{k}", "{r}"],
                          ["{r}", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "{K}", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("E5", "E4", board, "black")
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_white_king_backward():
    board = b.Chessboard([["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                          ["{p}", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "[K]", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "x", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("E4", "E3", board, "white")
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_black_king_backward():
    board = b.Chessboard([["x", "{k}", "{b}", "{Q}", "x", "{b}", "{k}", "{r}"],
                          ["{r}", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "{K}", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("E5", "E6", board, "black")
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_white_king_sideways():
    board = b.Chessboard([["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                          ["{p}", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "[K]", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "x", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("E4", "D4", board, "white")
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_black_king_sideways():
    board = b.Chessboard([["x", "{k}", "{b}", "{Q}", "x", "{b}", "{k}", "{r}"],
                          ["{r}", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "{K}", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("E5", "F5", board, "black")
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_white_king_diagonal():
    board = b.Chessboard([["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                          ["{p}", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "[K]", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "x", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("E4", "D5", board, "white")
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_black_king_diagonal():
    board = b.Chessboard([["x", "{k}", "{b}", "{Q}", "x", "{b}", "{k}", "{r}"],
                          ["{r}", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "{K}", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("E5", "F6", board, "black")
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_white_king_forward_blocked():
    board = b.Chessboard([["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                          ["{p}", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "[Q]", "x", "x", "x"],
                          ["x", "x", "x", "x", "[K]", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "x", "x", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("E4", "E5", board, "white")
    expected = False
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_black_king_forward_blocked():
    board = b.Chessboard([["x", "{k}", "{b}", "x", "x", "{b}", "{k}", "{r}"],
                          ["{r}", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "{K}", "x", "x", "x"],
                          ["x", "x", "x", "x", "{Q}", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("E5", "E4", board, "black")
    expected = False
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_white_king_backward_blocked():
    board = b.Chessboard([["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                          ["{p}", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "[K]", "x", "x", "x"],
                          ["x", "x", "x", "x", "[p]", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "x", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "x", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("E4", "E3", board, "white")
    expected = False
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_black_king_backward_blocked():
    board = b.Chessboard([["x", "{k}", "{b}", "{Q}", "x", "{b}", "{k}", "{r}"],
                          ["{r}", "{p}", "{p}", "{p}", "x", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "{p}", "x", "x", "x"],
                          ["x", "x", "x", "x", "{K}", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("E5", "E6", board, "black")
    expected = False
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_white_king_sideways_blocked():
    board = b.Chessboard([["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                          ["{p}", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "[p]", "[K]", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "x", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "x", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("E4", "D4", board, "white")
    expected = False
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_black_king_sideways_blocked():
    board = b.Chessboard([["x", "{k}", "{b}", "{Q}", "x", "{b}", "{k}", "{r}"],
                          ["{r}", "{p}", "{p}", "{p}", "{p}", "{p}", "x", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "{K}", "{p}", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("E5", "F5", board, "black")
    expected = False
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_white_king_diagonal_blocked():
    board = b.Chessboard([["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                          ["{p}", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "[Q]", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "[K]", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "x", "x", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("E4", "D5", board, "white")
    expected = False
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_black_king_diagonal_blocked():
    board = b.Chessboard([["x", "{k}", "{b}", "{Q}", "x", "{b}", "{k}", "{r}"],
                          ["{r}", "{p}", "{p}", "{p}", "{p}", "x", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "{p}", "x", "x"],
                          ["x", "x", "x", "x", "{K}", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("E5", "F6", board, "black")
    expected = False
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_white_king_forward_attack():
    board = b.Chessboard([["{r}", "{k}", "{b}", "x", "{K}", "{b}", "{k}", "{r}"],
                          ["{p}", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "{Q}", "x", "x", "x"],
                          ["x", "x", "x", "x", "[K]", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "x", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("E4", "E5", board, "white")
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_black_king_forward_attack():
    board = b.Chessboard([["x", "{k}", "{b}", "{Q}", "x", "{b}", "{k}", "{r}"],
                          ["{r}", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "{K}", "x", "x", "x"],
                          ["x", "x", "x", "x", "[Q]", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "x", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("E5", "E4", board, "black")
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_white_king_backward_attack():
    board = b.Chessboard([["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                          ["{p}", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "[K]", "x", "x", "x"],
                          ["x", "x", "x", "x", "{p}", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "x", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("E4", "E3", board, "white")
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_black_king_backward_attack():
    board = b.Chessboard([["x", "{k}", "{b}", "{Q}", "x", "{b}", "{k}", "{r}"],
                          ["{r}", "{p}", "{p}", "{p}", "x", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "[p]", "x", "x", "x"],
                          ["x", "x", "x", "x", "{K}", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("E5", "E6", board, "black")
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_white_king_sideways_attack():
    board = b.Chessboard([["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                          ["{p}", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "{p}", "[K]", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "x", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "x", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("E4", "D4", board, "white")
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_black_king_sideways_attack():
    board = b.Chessboard([["x", "{k}", "{b}", "{Q}", "x", "{b}", "{k}", "{r}"],
                          ["{r}", "{p}", "{p}", "{p}", "{p}", "{p}", "x", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "{K}", "[p]", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("E5", "F5", board, "black")
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_white_king_diagonal_attack():
    board = b.Chessboard([["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                          ["{p}", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "{Q}", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "[K]", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "x", "x", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("E4", "D5", board, "white")
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_black_king_diagonal_attack():
    board = b.Chessboard([["x", "{k}", "{b}", "{Q}", "x", "{b}", "{k}", "{r}"],
                          ["{r}", "{p}", "{p}", "{p}", "{p}", "x", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "[p]", "x", "x"],
                          ["x", "x", "x", "x", "{K}", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("E5", "F6", board, "black")
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_white_king_forward_two():
    board = b.Chessboard([["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                          ["{p}", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "[K]", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "x", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("E4", "E6", board, "white")
    expected = False
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_black_king_forward_two():
    board = b.Chessboard([["x", "{k}", "{b}", "{Q}", "x", "{b}", "{k}", "{r}"],
                          ["{r}", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "{K}", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("E5", "E3", board, "black")
    expected = False
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_white_king_backward_two():
    board = b.Chessboard([["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                          ["{p}", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "[K]", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "x", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "x", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("E4", "E2", board, "white")
    expected = False
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_black_king_backward_two():
    board = b.Chessboard([["x", "{k}", "{b}", "{Q}", "x", "{b}", "{k}", "{r}"],
                          ["{r}", "{p}", "{p}", "{p}", "x", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "{K}", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("E5", "E7", board, "black")
    expected = False
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_white_king_sideways_two():
    board = b.Chessboard([["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                          ["{p}", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "[K]", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "x", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("E4", "C4", board, "white")
    expected = False
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_black_king_sideways_two():
    board = b.Chessboard([["x", "{k}", "{b}", "{Q}", "x", "{b}", "{k}", "{r}"],
                          ["{r}", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "{K}", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("E5", "G5", board, "black")
    expected = False
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_white_king_diagonal_two():
    board = b.Chessboard([["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                          ["{p}", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "[K]", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "x", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("E4", "C6", board, "white")
    expected = False
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_black_king_diagonal_two():
    board = b.Chessboard([["x", "{k}", "{b}", "{Q}", "x", "{b}", "{k}", "{r}"],
                          ["{r}", "{p}", "{p}", "{p}", "{p}", "{p}", "x", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "{K}", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("E5", "G7", board, "black")


# @pytest.mark.skip("pending")
def test_validate_move_white_queen_forward():
    board = b.Chessboard([["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                          ["{p}", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "[Q]", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "x", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("E4", "E5", board, "white")


# @pytest.mark.skip("pending")
def test_validate_move_black_queen_forward():
    board = b.Chessboard([["x", "{k}", "{b}", "{Q}", "x", "{b}", "{k}", "{r}"],
                          ["{r}", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "{Q}", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("E5", "E4", board, "black")
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_white_queen_backward():
    board = b.Chessboard([["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                          ["{p}", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "[Q]", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "x", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("E4", "E3", board, "white")
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_black_queen_backward():
    board = b.Chessboard([["x", "{k}", "{b}", "{Q}", "x", "{b}", "{k}", "{r}"],
                          ["{r}", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "{Q}", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("E5", "E6", board, "black")
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_white_queen_sideways():
    board = b.Chessboard([["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                          ["{p}", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "[Q]", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "x", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("E4", "D4", board, "white")
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_black_queen_sideways():
    board = b.Chessboard([["x", "{k}", "{b}", "{Q}", "x", "{b}", "{k}", "{r}"],
                          ["{r}", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "{Q}", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("E5", "F5", board, "black")
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_white_queen_diagonal():
    board = b.Chessboard([["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                          ["{p}", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "[Q]", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "x", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("E4", "D5", board, "white")
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_black_queen_diagonal():
    board = b.Chessboard([["x", "{k}", "{b}", "{Q}", "x", "{b}", "{k}", "{r}"],
                          ["{r}", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "{Q}", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("E5", "F6", board, "black")
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_white_queen_forward_blocked():
    board = b.Chessboard([["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                          ["{p}", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "[K]", "x", "x", "x"],
                          ["x", "x", "x", "x", "[Q]", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "x", "x", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("E4", "E5", board, "white")


# @pytest.mark.skip("pending")
def test_validate_move_black_queen_forward_blocked():
    board = b.Chessboard([["x", "{k}", "{b}", "x", "x", "{b}", "{k}", "{r}"],
                          ["{r}", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "{Q}", "x", "x", "x"],
                          ["x", "x", "x", "x", "{K}", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("E5", "E4", board, "black")


# @pytest.mark.skip("pending")
def test_validate_move_white_queen_backward_blocked():
    board = b.Chessboard([["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                          ["{p}", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "[Q]", "x", "x", "x"],
                          ["x", "x", "x", "x", "[p]", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "x", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "x", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("E4", "E3", board, "white")


# @pytest.mark.skip("pending")
def test_validate_move_black_queen_backward_blocked():
    board = b.Chessboard([["x", "{k}", "{b}", "{Q}", "x", "{b}", "{k}", "{r}"],
                          ["{r}", "{p}", "{p}", "{p}", "x", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "{p}", "x", "x", "x"],
                          ["x", "x", "x", "x", "{Q}", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("E5", "E6", board, "black")
    expected = False
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_white_queen_sideways_blocked():
    board = b.Chessboard([["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                          ["{p}", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "[p]", "[Q]", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "x", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "x", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("E4", "D4", board, "white")
    expected = False
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_black_queen_sideways_blocked():
    board = b.Chessboard([["x", "{k}", "{b}", "{Q}", "x", "{b}", "{k}", "{r}"],
                          ["{r}", "{p}", "{p}", "{p}", "{p}", "{p}", "x", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "{Q}", "{p}", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("E5", "F5", board, "black")
    expected = False
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_white_queen_diagonal_blocked():
    board = b.Chessboard([["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                          ["{p}", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "[K]", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "[Q]", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "x", "x", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("E4", "D5", board, "white")
    expected = False
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_black_queen_diagonal_blocked():
    board = b.Chessboard([["x", "{k}", "{b}", "{Q}", "x", "{b}", "{k}", "{r}"],
                          ["{r}", "{p}", "{p}", "{p}", "{p}", "x", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "{p}", "x", "x"],
                          ["x", "x", "x", "x", "{Q}", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("E5", "F6", board, "black")
    expected = False
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_white_queen_forward_attack():
    board = b.Chessboard([["{r}", "{k}", "{b}", "x", "{K}", "{b}", "{k}", "{r}"],
                          ["{p}", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "{K}", "x", "x", "x"],
                          ["x", "x", "x", "x", "[Q]", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "x", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("E4", "E5", board, "white")
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_black_queen_forward_attack():
    board = b.Chessboard([["x", "{k}", "{b}", "{Q}", "x", "{b}", "{k}", "{r}"],
                          ["{r}", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "{Q}", "x", "x", "x"],
                          ["x", "x", "x", "x", "[K]", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "x", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("E5", "E4", board, "black")
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_white_queen_backward_attack():
    board = b.Chessboard([["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                          ["{p}", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "[Q]", "x", "x", "x"],
                          ["x", "x", "x", "x", "{p}", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "x", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("E4", "E3", board, "white")
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_black_queen_backward_attack():
    board = b.Chessboard([["x", "{k}", "{b}", "{Q}", "x", "{b}", "{k}", "{r}"],
                          ["{r}", "{p}", "{p}", "{p}", "x", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "[p]", "x", "x", "x"],
                          ["x", "x", "x", "x", "{Q}", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("E5", "E6", board, "black")
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_white_queen_sideways_attack():
    board = b.Chessboard([["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                          ["{p}", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "{p}", "[Q]", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "x", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "x", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("E4", "D4", board, "white")
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_black_queen_sideways_attack():
    board = b.Chessboard([["x", "{k}", "{b}", "{Q}", "x", "{b}", "{k}", "{r}"],
                          ["{r}", "{p}", "{p}", "{p}", "{p}", "{p}", "x", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "{Q}", "[p]", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("E5", "F5", board, "black")
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_white_queen_diagonal_attack():
    board = b.Chessboard([["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                          ["{p}", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "{Q}", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "[Q]", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "x", "x", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("E4", "D5", board, "white")
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_black_queen_diagonal_attack():
    board = b.Chessboard([["x", "{k}", "{b}", "{Q}", "x", "{b}", "{k}", "{r}"],
                          ["{r}", "{p}", "{p}", "{p}", "{p}", "x", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "[p]", "x", "x"],
                          ["x", "x", "x", "x", "{Q}", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("E5", "F6", board, "black")
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_white_queen_forward_three():
    board = b.Chessboard([["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                          ["{p}", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "[Q]", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "x", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("E4", "E7", board, "white")
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_black_queen_forward_three():
    board = b.Chessboard([["x", "{k}", "{b}", "{Q}", "x", "{b}", "{k}", "{r}"],
                          ["{r}", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "{Q}", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("E5", "E2", board, "black")
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_white_queen_backward_three():
    board = b.Chessboard([["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                          ["{p}", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "[Q]", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "x", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "x", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("E4", "E1", board, "white")
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_black_queen_backward_three():
    board = b.Chessboard([["x", "{k}", "{b}", "{Q}", "x", "{b}", "{k}", "{r}"],
                          ["{r}", "{p}", "{p}", "{p}", "x", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "{Q}", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("E5", "E8", board, "black")
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_white_queen_sideways_three():
    board = b.Chessboard([["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                          ["{p}", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "[Q]", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "x", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("E4", "B4", board, "white")
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_black_queen_sideways_three():
    board = b.Chessboard([["x", "{k}", "{b}", "{Q}", "x", "{b}", "{k}", "{r}"],
                          ["{r}", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "{Q}", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("E5", "H5", board, "black")
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_white_queen_diagonal_three():
    board = b.Chessboard([["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                          ["{p}", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "[Q]", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "x", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("E4", "B7", board, "white")
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_black_queen_diagonal_three():
    board = b.Chessboard([["x", "{k}", "{b}", "{Q}", "x", "{b}", "{k}", "x"],
                          ["{r}", "{p}", "{p}", "{p}", "{p}", "{p}", "x", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "{Q}", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("E5", "H8", board, "black")
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_white_bishop_diagonal():
    board = b.Chessboard([["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                          ["{p}", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "[b]", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "x", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("C4", "D5", board, "white")
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_black_bishop_diagonal():
    board = b.Chessboard([["{r}", "{k}", "x", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                          ["x", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "{b}", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("C5", "D4", board, "black")
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_white_bishop_diagonal_three():
    board = b.Chessboard([["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                          ["{p}", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "[b]", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "x", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("C4", "F7", board, "white")
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_black_bishop_diagonal_three():
    board = b.Chessboard([["{r}", "{k}", "x", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                          ["x", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "{b}", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("C5", "F2", board, "black")
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_white_bishop_diagonal_blocked():
    board = b.Chessboard([["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                          ["{p}", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "[x]", "x", "x", "x", "x"],
                          ["x", "x", "[b]", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "x", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("C4", "D5", board, "white")
    expected = False
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_black_bishop_diagonal_blocked():
    board = b.Chessboard([["{r}", "{k}", "x", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                          ["x", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "{b}", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "{p}", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("C5", "D4", board, "black")
    expected = False
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_white_bishop_diagonal_attack():
    board = b.Chessboard([["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                          ["{p}", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "{x}", "x", "x", "x", "x"],
                          ["x", "x", "[b]", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "x", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("C4", "D5", board, "white")
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_black_bishop_diagonal_attack():
    board = b.Chessboard([["{r}", "{k}", "x", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                          ["x", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "{b}", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "[p]", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("C5", "D4", board, "black")
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_white_bishop_vertical():
    board = b.Chessboard([["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                          ["{p}", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "[b]", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "x", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("C4", "C5", board, "white")
    expected = False
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_black_bishop_vertical():
    board = b.Chessboard([["{r}", "{k}", "x", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                          ["x", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "{b}", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("C5", "C4", board, "black")
    expected = False
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_white_bishop_horizontal():
    board = b.Chessboard([["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                          ["{p}", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "[b]", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "x", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("C4", "B4", board, "white")
    expected = False
    assert actual == expected


# @pytest.mark.skip("pending")
def test_validate_move_black_bishop_horizontal():
    board = b.Chessboard([["{r}", "{k}", "x", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                          ["x", "{p}", "{p}", "{p}",
                              "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "{b}", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("C5", "D5", board, "black")
    expected = False
    assert actual == expected


@pytest.mark.parametrize(
    "start,end,expected",
    [
        ("D4", "C6", True),
        ("D4", "E6", True),
        ("D4", "C2", True),
        ("D4", "E2", True),
        ("D4", "B3", True),
        ("D4", "B5", True),
        ("D4", "F3", True),
        ("D4", "F5", True)
    ]
)
# @pytest.mark.skip("pending")
def test_validate_move_white_knight(start, end, expected):
    board = b.Chessboard([["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "[k]", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"]])
    actual = c.validate_move(start, end, board, "white")
    assert actual == expected


@pytest.mark.parametrize(
    "start,end,expected",
    [
        ("D4", "C6", True),
        ("D4", "E6", True),
        ("D4", "C2", True),
        ("D4", "E2", True),
        ("D4", "B3", True),
        ("D4", "B5", True),
        ("D4", "F3", True),
        ("D4", "F5", True)
    ]
)
# @pytest.mark.skip("pending")
def test_validate_move_black_knight(start, end, expected):
    board = b.Chessboard([["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "{k}", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"]])
    actual = c.validate_move(start, end, board, "black")
    assert actual == expected


@pytest.mark.parametrize(
    "start,end,expected",
    [
        ("D4", "C6", False),
        ("D4", "E6", False),
        ("D4", "C2", False),
        ("D4", "E2", False),
        ("D4", "B3", False),
        ("D4", "B5", False),
        ("D4", "F3", False),
        ("D4", "F5", False)
    ]
)
# @pytest.mark.skip("pending")
def test_validate_move_white_knight_blocked(start, end, expected):
    board = b.Chessboard([["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "[p]", "x", "[p]", "x", "x", "x"],
                          ["x", "[p]", "x", "x", "x", "[p]", "x", "x"],
                          ["x", "x", "x", "[k]", "x", "x", "x", "x"],
                          ["x", "[p]", "x", "x", "x", "[p]", "x", "x"],
                          ["x", "x", "[p]", "x", "[p]", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"]])
    actual = c.validate_move(start, end, board, "white")
    assert actual == expected


@pytest.mark.parametrize(
    "start,end,expected",
    [
        ("D4", "C6", False),
        ("D4", "E6", False),
        ("D4", "C2", False),
        ("D4", "E2", False),
        ("D4", "B3", False),
        ("D4", "B5", False),
        ("D4", "F3", False),
        ("D4", "F5", False)
    ]
)
# @pytest.mark.skip("pending")
def test_validate_move_black_knight_blocked(start, end, expected):
    board = b.Chessboard([["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "{p}", "x", "{p}", "x", "x", "x"],
                          ["x", "{p}", "x", "x", "x", "{p}", "x", "x"],
                          ["x", "x", "x", "{k}", "x", "x", "x", "x"],
                          ["x", "{p}", "x", "x", "x", "{p}", "x", "x"],
                          ["x", "x", "{p}", "x", "{p}", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"]])
    actual = c.validate_move(start, end, board, "black")
    assert actual == expected


@pytest.mark.parametrize(
    "start,end,expected",
    [
        ("D4", "C6", True),
        ("D4", "E6", True),
        ("D4", "C2", True),
        ("D4", "E2", True),
        ("D4", "B3", True),
        ("D4", "B5", True),
        ("D4", "F3", True),
        ("D4", "F5", True)
    ]
)
# @pytest.mark.skip("pending")
def test_validate_move_white_knight_attack(start, end, expected):
    board = b.Chessboard([["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "{p}", "x", "{p}", "x", "x", "x"],
                          ["x", "{p}", "x", "x", "x", "{p}", "x", "x"],
                          ["x", "x", "x", "[k]", "x", "x", "x", "x"],
                          ["x", "{p}", "x", "x", "x", "{p}", "x", "x"],
                          ["x", "x", "{p}", "x", "{p}", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"]])
    actual = c.validate_move(start, end, board, "white")
    assert actual == expected


@pytest.mark.parametrize(
    "start,end,expected",
    [
        ("D4", "C6", True),
        ("D4", "E6", True),
        ("D4", "C2", True),
        ("D4", "E2", True),
        ("D4", "B3", True),
        ("D4", "B5", True),
        ("D4", "F3", True),
        ("D4", "F5", True)
    ]
)
# @pytest.mark.skip("pending")
def test_validate_move_black_knight_attack(start, end, expected):
    board = b.Chessboard([["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "[p]", "x", "[p]", "x", "x", "x"],
                          ["x", "[p]", "x", "x", "x", "[p]", "x", "x"],
                          ["x", "x", "x", "{k}", "x", "x", "x", "x"],
                          ["x", "[p]", "x", "x", "x", "[p]", "x", "x"],
                          ["x", "x", "[p]", "x", "[p]", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"]])
    actual = c.validate_move(start, end, board, "black")
    assert actual == expected


# @pytest.mark.skip("pending")
def test_move_pawn(standard_board):
    actual = standard_board.board
    c.move_piece("A2", "A3", actual, False)
    expected = [["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                ["{p}", "{p}", "{p}", "{p}", "{p}", "{p}", "{p}", "{p}"],
                ["x",    "x",   "x",   "x",   "x",   "x",   "x",   "x"],
                ["x",    "x",   "x",   "x",   "x",   "x",   "x",   "x"],
                ["x",    "x",   "x",   "x",   "x",   "x",   "x",   "x"],
                ["[p]",  "x",   "x",   "x",   "x",   "x",   "x",   "x"],
                ["x",  "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]]
    assert actual == expected


# @pytest.mark.skip("pending")
def test_move_knight(standard_board):
    actual = standard_board.board
    c.move_piece("B1", "C3", actual, False)
    expected = [["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                ["{p}", "{p}", "{p}", "{p}", "{p}", "{p}", "{p}", "{p}"],
                ["x",    "x",   "x",   "x",   "x",   "x",   "x",   "x"],
                ["x",    "x",   "x",   "x",   "x",   "x",   "x",   "x"],
                ["x",    "x",   "x",   "x",   "x",   "x",   "x",   "x"],
                ["x",    "x", "[k]",   "x",   "x",   "x",   "x",   "x"],
                ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                ["[r]",  "x",  "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]]
    assert actual == expected


# @pytest.mark.skip("pending")
def test_move_rook(pawns_forward_board):
    actual = pawns_forward_board.board
    c.move_piece("A1", "A3", actual, False)
    expected = [["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                ["x",    "x",   "x",   "x",   "x",   "x",   "x",   "x"],
                ["x",    "x",   "x",   "x",   "x",   "x",   "x",   "x"],
                ["{p}", "{p}", "{p}", "{p}", "{p}", "{p}", "{p}", "{p}"],
                ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                ["[r]",    "x",   "x",   "x",   "x",   "x",   "x",   "x"],
                ["x",    "x",   "x",   "x",   "x",   "x",   "x",   "x"],
                ["x", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]]
    assert actual == expected


# @pytest.mark.skip("pending")
def test_move_bishop(pawns_forward_board):
    actual = pawns_forward_board.board
    c.move_piece("C1", "A3", actual, False)
    expected = [["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                ["x",    "x",   "x",   "x",   "x",   "x",   "x",   "x"],
                ["x",    "x",   "x",   "x",   "x",   "x",   "x",   "x"],
                ["{p}", "{p}", "{p}", "{p}", "{p}", "{p}", "{p}", "{p}"],
                ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                ["[b]",    "x",   "x",   "x",   "x",   "x",   "x",   "x"],
                ["x",    "x",   "x",   "x",   "x",   "x",   "x",   "x"],
                ["[r]", "[k]", "x", "[Q]", "[K]", "[b]", "[k]", "[r]"]]
    assert actual == expected


# @pytest.mark.skip("pending")
def test_move_queen(pawns_forward_board):
    actual = pawns_forward_board.board
    c.move_piece("D1", "F3", actual, False)
    expected = [["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                ["x", "x", "x", "x", "x", "x", "x", "x"],
                ["x", "x", "x", "x", "x", "x", "x", "x"],
                ["{p}", "{p}", "{p}", "{p}", "{p}", "{p}", "{p}", "{p}"],
                ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                ["x", "x", "x", "x", "x", "[Q]", "x", "x"],
                ["x", "x", "x", "x", "x", "x", "x", "x"],
                ["[r]", "[k]", "[b]", "x", "[K]", "[b]", "[k]", "[r]"]]
    assert actual == expected


# @pytest.mark.skip("pending")
def test_move_king(pawns_forward_board):
    actual = pawns_forward_board.board
    c.move_piece("E1", "E2", actual, False)
    expected = [["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                ["x", "x", "x", "x", "x", "x", "x", "x"],
                ["x", "x", "x", "x", "x", "x", "x", "x"],
                ["{p}", "{p}", "{p}", "{p}", "{p}", "{p}", "{p}", "{p}"],
                ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                ["x", "x", "x", "x", "x", "x", "x", "x"],
                ["x", "x", "x", "x", "[K]", "x", "x", "x"],
                ["[r]", "[k]", "[b]", "[Q]", "x", "[b]", "[k]", "[r]"]]
    assert actual == expected


# @pytest.mark.skip("pending")
def test_find_black_king(standard_board):
    actual = c.find_king("black", standard_board)
    expected = (0, 4)
    assert actual == expected


# @pytest.mark.skip("pending")
def test_find_white_king(standard_board):
    actual = c.find_king("white", standard_board)
    expected = (7, 4)
    assert actual == expected


# @pytest.mark.skip("pending")
def test_black_king_not_check(standard_board):
    actual = c.check_check("black", standard_board)
    expected = False
    assert actual == expected


# @pytest.mark.skip("pending")
def test_black_king_check(black_in_check_not_checkmate):
    actual = c.check_check("black", black_in_check_not_checkmate)
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_black_king_check_not_checkmate(black_in_check_not_checkmate):
    actual = c.check_checkmate("black", black_in_check_not_checkmate)
    expected = False
    assert actual == expected


# @pytest.mark.skip("pending")
def test_black_king_checkmate(black_in_checkmate):
    actual = c.check_checkmate("black", black_in_checkmate)
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_white_king_not_check(standard_board):
    actual = c.check_check("white", standard_board)
    expected = False
    assert actual == expected


# @pytest.mark.skip("pending")
def test_white_king_check(white_in_check_not_checkmate):
    actual = c.check_check("white", white_in_check_not_checkmate)
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_white_king_check_not_checkmate(white_in_check_not_checkmate):
    actual = c.check_checkmate("white", white_in_check_not_checkmate)
    expected = False
    assert actual == expected


# @pytest.mark.skip("pending")
def test_white_king_checkmate(white_in_checkmate):
    actual = c.check_checkmate("white", white_in_checkmate)
    expected = True
    assert actual == expected


@pytest.fixture
def standard_board():
    standard_board = b.Chessboard([["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                                   ["{p}", "{p}", "{p}", "{p}",
                                       "{p}", "{p}", "{p}", "{p}"],
                                   ["x",    "x",   "x",   "x",
                                       "x",   "x",   "x",   "x"],
                                   ["x",    "x",   "x",   "x",
                                       "x",   "x",   "x",   "x"],
                                   ["x",    "x",   "x",   "x",
                                       "x",   "x",   "x",   "x"],
                                   ["x",    "x",   "x",   "x",
                                       "x",   "x",   "x",   "x"],
                                   ["[p]", "[p]", "[p]", "[p]",
                                       "[p]", "[p]", "[p]", "[p]"],
                                   ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    return standard_board


@pytest.fixture
def black_in_checkmate():
    black_in_checkmate = b.Chessboard([["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                                       ["x",   "{p}", "{p}", "{p}",
                                           "{p}", "[Q]", "{p}", "{p}"],
                                       ["x",    "x",   "x",   "x",
                                           "x",   "x",   "x",   "x"],
                                       ["x",    "x",   "x",   "x",
                                           "x",   "x",   "x",   "x"],
                                       ["{p}",  "x",  "[b]",  "x",
                                           "x",   "x",   "x",   "x"],
                                       ["x",    "x",   "x",   "x",
                                           "[p]",  "x",   "x",   "x"],
                                       ["[p]", "[p]", "[p]", "[p]",
                                           "x",  "[p]", "[p]", "[p]"],
                                       ["[r]", "[k]", "[b]",  "x", "[K]",  "x", "[k]", "[r]"]])
    return black_in_checkmate


@pytest.fixture
def pawns_forward_board():
    pawns_forward_board = b.Chessboard([["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                                        ["x",    "x",   "x",   "x",
                                            "x",   "x",   "x",   "x"],
                                        ["x",    "x",   "x",   "x",
                                            "x",   "x",   "x",   "x"],
                                        ["{p}", "{p}", "{p}", "{p}",
                                            "{p}", "{p}", "{p}", "{p}"],
                                        ["[p]", "[p]", "[p]", "[p]",
                                            "[p]", "[p]", "[p]", "[p]"],
                                        ["x",    "x",   "x",   "x",
                                            "x",   "x",   "x",   "x"],
                                        ["x",    "x",   "x",   "x",
                                            "x",   "x",   "x",   "x"],
                                        ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    return pawns_forward_board


@pytest.fixture
def black_in_check_not_checkmate():
    black_in_check_not_checkmate = b.Chessboard([["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                                                 ["x",  "{p}", "{p}", "{p}",
                                                     "{p}", "[Q]", "{p}", "{p}"],
                                                 ["x",    "x",   "x",   "x",
                                                     "x",   "x",   "x",   "x"],
                                                 ["x",    "x",   "x",   "x",
                                                     "x",   "x",   "x",   "x"],
                                                 ["{p}",  "x",   "x",   "x",
                                                     "x",   "x",   "x",   "x"],
                                                 ["x",    "x",   "x",   "x",
                                                     "[p]",  "x",   "x",   "x"],
                                                 ["[p]", "[p]", "[p]", "[p]",
                                                     "x", "[p]", "[p]", "[p]"],
                                                 ["[r]", "[k]", "[b]",  "x", "[K]", "[b]", "[k]", "[r]"]])
    return black_in_check_not_checkmate


@pytest.fixture
def white_in_check_not_checkmate():
    white_in_check_not_checkmate = b.Chessboard([["{r}", "{k}", "{b}",   "x", "{K}", "{b}", "{k}", "{r}"],
                                                 ["{p}",  "{p}", "{p}", "{p}",
                                                     "x", "{p}", "{p}", "{p}"],
                                                 ["x",    "[p]", "x",   "x",
                                                     "{p}", "x",   "x",   "x"],
                                                 ["x",    "x",   "x",   "x",
                                                     "x",   "x",   "x",   "x"],
                                                 ["x",    "x",   "x",   "x",
                                                     "x",   "x",   "x",   "x"],
                                                 ["x",    "x",   "x",   "x",
                                                     "x",  "x",   "x",   "x"],
                                                 ["[p]", "x", "[p]", "[p]",
                                                     "[p]", "{Q}", "[p]", "[p]"],
                                                 ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    return white_in_check_not_checkmate


@pytest.fixture
def white_in_checkmate():
    white_in_checkmate = b.Chessboard([["{r}", "{k}", "{b}",   "x", "{K}", "x", "{k}", "{r}"],
                                       ["{p}",  "{p}", "{p}", "{p}",
                                           "x", "{p}", "{p}", "{p}"],
                                       ["x",    "[p]", "x",   "x",
                                           "{p}", "x",   "x",   "x"],
                                       ["x",    "x",   "{b}", "x",
                                           "x",   "x",   "x",   "x"],
                                       ["x",    "x",   "x",   "x",
                                           "x",   "x",   "x",   "x"],
                                       ["x",    "x",   "[p]", "x",
                                           "x",  "x",   "x",   "x"],
                                       ["[p]", "x", "x", "[p]", "[p]",
                                           "{Q}", "[p]", "[p]"],
                                       ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    return white_in_checkmate
