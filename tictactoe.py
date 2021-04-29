"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy
import random

X = "X"
O = "O"
EMPTY = None
act = []

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    numO = 0
    numX = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                numX += 1
            if board[i][j] == O:
                numO += 1
    if numO == 0 and numX == 0:
        return X
    if numO < numX:
        return O
    return X



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possiblemovess = set([])
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possiblemovess.add((i, j))
    return possiblemovess



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    s = deepcopy(board)
    if s[action[0]][action[1]] != EMPTY:
        raise Exception
    currplayer = player(s)
    s[action[0]][action[1]] = currplayer
    return s


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for i in range(3):
        if board[i].count(X) == 3:
            return X
        elif board[i].count(O) == 3:
            return O
    for i in range(3):
        if board[0][i] == X and board[1][i] == X and board[2][i] == X:
            return X
        if board[0][i] == O and board[1][i] == O and board[2][i] == O:
            return O
    diag1 = [board[0][0], board[1][1], board[2][2]]
    diag2 = [board[0][2], board[1][1], board[2][0]]
    if diag1.count(X) == 3:
        return X
    elif diag1.count(O) == 3:
        return O
    if diag2.count(X) == 3:
        return X
    elif diag2.count(O) == 3:
        return O
    return None



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0

def maxvalue(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    possible_states = actions(board)
    for action in possible_states:
        v = max(v, minvalue(result(board, action)))
    return v

def minvalue(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    possible_states = actions(board)
    for action in possible_states:
        v = min(v, maxvalue(result(board, action)))
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if board == initial_state():
        return (random.choice(range(3)), random.choice(range(3)))
    if terminal(board):
        return None
    currplayer = player(board)
    possible_states = actions(board)
    if currplayer == X:
        bestofallv = -math.inf
        for action in possible_states:
            maxv = minvalue(result(board, action))
            if maxv > bestofallv:
                bestofallv = maxv
                if len(act) != 0:
                    act.pop()
                act.append(action)
    else:
        bestofallv = math.inf
        for action in possible_states:
            minv = maxvalue(result(board, action))
            if minv < bestofallv:
                bestofallv = minv
                if len(act) != 0:
                    act.pop()
                act.append(action)

    return act[0]

