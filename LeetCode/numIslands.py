class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0 
        count = 0
        self.height = len(grid)
        self.width = len(grid[0])
        self.grid = grid
        for r in range(self.height):
            for c in range(self.width):
                if grid[r][c] == '1':
                    self.mark(r, c)
                    count += 1
        return count
    def mark(self, r, c):
        self.grid[r][c] = 'x'
        if  r > 0 and self.grid[r-1][c] == '1':
            self.mark(r-1, c)
        if  c > 0 and self.grid[r][c-1] == '1':
            self.mark(r, c-1)
        if r < self.height - 1 and self.grid[r+1][c] == '1':
            self.mark(r+1, c)
        if c < self.width - 1 and self.grid[r][c+1] == '1' :
            self.mark(r, c+1)
