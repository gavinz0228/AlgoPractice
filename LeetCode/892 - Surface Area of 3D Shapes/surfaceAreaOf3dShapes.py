from typing import List


class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.height = len(grid)
        self.width = len(grid[0])
        sol = 0
        for r in range(self.height):
            for c in range(self.width):
                cur = grid[r][c]
                sol += max(0, cur - self.getHeight(r + 1, c))
                sol += max(0, cur - self.getHeight(r - 1, c))
                sol += max(0, cur - self.getHeight(r, c + 1))
                sol += max(0, cur - self.getHeight(r, c - 1))
                if cur != 0:
                    sol += 2
        return sol

    def getHeight(self, r, c):
        if r < 0 or r == self.height or c < 0 or c == self.width:
            return 0
        else:
            return self.grid[r][c]
