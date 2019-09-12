from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.height, self.width =n, n
        self.sol = []
        self.rowMark = set()
        self.colMark = set()
        self.diagLeft = set()
        self.diagRight = set() 
        self.aux(0, 0, n, [] )
        return self.sol

    def aux(self, row, col, num_queen, curr):
        if num_queen == 0:
            board =  [ [ "." for j in range(self.width)] for i in range(self.height)]
            for r,c in curr:
                board[r][c] = 'Q'
            self.sol.append([ "".join(board[i][:]) for i in range(self.width)])
            return
        for i in range(row, self.height):
            for j in range(col, self.width):
                if j not in self.colMark and i not in self.rowMark and i+j not in self.diagLeft and j-i not in self.diagRight:
                    curr.append((i,j))
                    self.colMark.add(j)
                    self.rowMark.add(i)
                    self.diagLeft.add(i+j)
                    self.diagRight.add(j-i)
                    self.aux(i, j + 1 , num_queen - 1, curr)
                    curr.pop()
                    self.colMark.remove(j)
                    self.rowMark.remove(i)
                    self.diagLeft.remove(i+j)
                    self.diagRight.remove(j-i)
                        
            col = 0


res = Solution().solveNQueens(9)
print(res)