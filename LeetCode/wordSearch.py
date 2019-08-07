class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.height = len(board)
        self.width = len(board[0])
        for i, row in enumerate(board):
            for j, val in enumerate(row):
                if val == word[0]:
                    if len(word) == 1:
                        return True
                    res = self.search(i, j, word, 0, set())
                    if res:
                        return True
        return False
    def search(self, r, c, word,i , visited):
        if (r,c,) in visited:
            return False
        visited.add((r,c,))
        if word[i] == self.board[r][c]: 
            if i == len(word) - 1:
                return True
            result = []
            if r > 0:
                up = self.search(r - 1, c , word, i+1, visited)
                result.append(up)
            if r < self.height -1:
                down = self.search(r + 1, c , word, i+1, visited)
                result.append(down)
            if c > 0:
                left = self.search(r , c- 1 , word, i+1, visited)  
                result.append(left)
            if c < self.width - 1:
                right = self.search(r , c + 1 , word, i+1, visited)
                result.append(right)
            if any(result):
                return True
            else:
                visited.remove( (r, c))
        else:
            visited.remove( (r, c))
            return False
        
