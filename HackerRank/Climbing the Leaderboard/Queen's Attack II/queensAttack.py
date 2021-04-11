"""
You will be given a square chess board with one queen and a number of obstacles placed on it. Determine how many squares the queen can attack.

A queen is standing on an  chessboard. The chess board's rows are numbered from  to , going from bottom to top. Its columns are numbered from  to , going from left to right. Each square is referenced by a tuple, , describing the row, , and column, , where the square is located.

The queen is standing at position . In a single move, she can attack any square in any of the eight directions (left, right, up, down, and the four diagonals). In the diagram below, the green circles denote all the cells the queen can attack from :
"""

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    obs = set([(o[0], o[1],) for o in obstacles])
    return countSpot(n, r_q, c_q, 1, 1, obs) \
        + countSpot(n, r_q, c_q, -1, -1, obs) \
        + countSpot(n, r_q, c_q, 1, -1, obs) \
        + countSpot(n, r_q, c_q, -1, 1, obs) \
        + countSpot(n, r_q, c_q, 0, 1, obs) \
        + countSpot(n, r_q, c_q, 0, -1, obs) \
        + countSpot(n, r_q, c_q, 1, 0, obs) \
        + countSpot(n, r_q, c_q, -1, 0, obs) 
def checkBound(n, r, c):
    return r >= 1 and r <= n and c >= 1 and c <= n
def countSpot(n, r, c, r_inc, c_inc, obs):
    res = 0
    cur_r = r + r_inc
    cur_c = c + c_inc
    while True:
        if (not checkBound(n, cur_r, cur_c) ) or ((cur_r, cur_c,) in obs):
            return res
        res += 1
        cur_r += r_inc
        cur_c += c_inc
