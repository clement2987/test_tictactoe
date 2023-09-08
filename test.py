import pytest

from tictactoe import *

board1 = [[O, EMPTY, X],
            [EMPTY, EMPTY, EMPTY],
            [X, EMPTY, EMPTY]]

board2 = [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

board3 = [[O, X, EMPTY],
            [O, X, EMPTY],
            [X, EMPTY, EMPTY]]

board4 = [[O, EMPTY, O],
            [X, X, EMPTY],
            [X, X, O]]

board5 = [[O, O, O],
            [X, X, EMPTY],
            [X, X, O]]

board6 = [[O, EMPTY, X],
            [EMPTY, X, EMPTY],
            [X, EMPTY, O]]

board7 = [[O, X, X],
            [X, O, O],
            [X, O, X]]

board8 = [[EMPTY, EMPTY, EMPTY],
            [O, EMPTY, EMPTY],
            [X, O, X]]

board9 = [[EMPTY, O, EMPTY],
            [EMPTY, X, EMPTY],
            [O, X, EMPTY]]

board10 = [[EMPTY, EMPTY, EMPTY],
            [EMPTY, X, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

board11 = [[X, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

board12 = [[X, EMPTY, O],
            [EMPTY, EMPTY, EMPTY],
            [O, EMPTY, X]]

def test_player():
    assert player(board1) == 'O'
    assert player(board2) == 'X'
    assert player(board3) == 'O'

def test_actions():
    assert actions(board4) == {(0, 1), (1, 2)}
    assert actions(board3) == {(0, 2), (1, 2), (2, 1), (2, 2)}

def test_result():
    assert result(board4, (0, 1)) == board5
    #with pytest.raises(MistakeInActionsError):
    #    assert result(board4, (0, 0))

def test_winner():
    assert winner(board5) == 'O'
    assert winner(board6) == 'X'
    assert winner(board4) == None

def test_terminal():
    assert terminal(board5) == True
    assert terminal(board7) == True
    assert terminal(board4) == False

def test_utility():
    assert utility(board6) == 1
    assert utility(board5) == -1
    assert utility(board7) == 0

def test_minimax():
    assert minimax(board11) == (1, 1)
    assert minimax(board12) == (1, 1)

def test_max_value():
    assert max_value(board8) == 1
    assert max_value(board4) == -1
    assert max_value(board9) == 0
    assert max_value(board1) == 1
    assert max_value(board10) == 0