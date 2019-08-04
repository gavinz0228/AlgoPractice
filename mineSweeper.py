class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        self.width = len(board[0])
        self.height = len(board)
        self.board = board
        self. visited = set()
        if self.isMine(click[0], click[1]) == 1:
            self.board[click[0]][click[1]] = 'X'
            return board
        self.aux(click[0], click[1])
        return board
    def aux(self, i, j):
        if i >= self.height or i< 0 or j >= self.width or j < 0:
            return
        if (i, j) in self.visited:
            return
        self.visited.add((i, j))
        if self.isMine(i,j) == 1:
            return
        mcount = self.getNumMines(i,j)
        if mcount > 0:
            self.board[i][j] = str(mcount)
            return
        self.board[i][j] = 'B'
        self.aux(i - 1, j)
        self.aux(i + 1, j)
        self.aux(i , j - 1)
        self.aux(i , j + 1)
        self.aux(i + 1, j + 1)
        self.aux(i + 1, j - 1)
        self.aux(i - 1, j + 1)
        self.aux(i - 1, j - 1)

    def isMine(self, i, j):
        if i>= 0 and i< self.height and j >= 0 and j < self.width:
            if self.board[i][j] == 'M':
                return 1
        return 0
            
    def getNumMines(self, i, j):
        count = self.isMine(i+1, j)
        count += self.isMine(i, j+1)
        count += self.isMine(i-1, j)
        count += self.isMine(i, j-1)
        count += self.isMine(i+1, j-1)
        count += self.isMine(i+1, j+1)
        count += self.isMine(i-1, j+1)
        count += self.isMine(i-1, j-1)
        return count
    
