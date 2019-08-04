
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.height = len(board)
        self.width = len(board[0])
        self.aux(0,0)
        return self.board
    def aux(self, r, c):
        for i in range(r, self.height):
            for j in range(c, self.width):
                if self.board[i][j] == '.':
                    for n in range(1, 10):
                        temp = str(n)
                        if self.fit(i,j, temp):
                            self.board[i][j] = temp
                            res = self.aux(i,j)
                            if res:
                                return True
                            self.board[i][j] = '.'
                    return False
            c = 0
        return True

    def fit(self, r, c, val):
        if val in set( self.board[r][i] for i in range(9)):
            return False
        if val in set( self.board[i][c] for i in range(9) ):
            return False
        group_r = int( r / 3) * 3
        group_c = int (c / 3) * 3
        if val in set(self.board[i][j] for i in range(group_r, group_r+3) for j in range(group_c, group_c+3)):
            return False
        return True
    
