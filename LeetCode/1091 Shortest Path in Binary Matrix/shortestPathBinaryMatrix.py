import collections
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        r = 0
        c = 0
        self.grid = grid
        self.width = len(grid)
        tar = self.width - 1
        q = collections.deque()
        if grid[r][c] == 0:
            q.appendleft((r, c, 1,))
        
        while q:

            r, c, steps = q.popleft()
            if r == tar and c == tar:
                return steps
            grid[r][c] = 1
            
            if self.isValid(r + 1, c):
                q.append((r + 1, c, steps + 1,))
                grid[r + 1][c] = 1
                
            if self.isValid(r + 1, c + 1):
                q.append((r + 1, c + 1, steps + 1,))
                grid[r + 1][c + 1] = 1
                
            if self.isValid(r, c + 1):
                q.append((r, c + 1, steps + 1,))
                grid[r][c + 1] = 1

            if self.isValid(r + 1, c - 1):
                q.append((r + 1, c - 1, steps + 1,))
                grid[r + 1][c - 1] = 1
                
            if self.isValid(r - 1, c):
                q.append((r - 1, c, steps + 1,))
                grid[r - 1][c] = 1
                
            if self.isValid(r, c - 1):
                q.append((r, c - 1, steps + 1,))
                grid[r][c - 1] = 1
                
            if self.isValid(r - 1, c - 1):
                q.append((r - 1, c - 1, steps + 1,))
                
            if self.isValid(r - 1, c + 1):
                q.append((r - 1, c + 1, steps + 1,))
                grid[r - 1][c + 1] = 1
            
            
        return -1
            
    def isValid(self, r, c):
        return self.width > r >= 0 and self.width > c >= 0 and self.grid[r][c] == 0 
