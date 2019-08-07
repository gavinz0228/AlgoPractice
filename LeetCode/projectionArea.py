class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])
        empty_top = 0
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 0:
                    empty_top += 1
        top = height * width - empty_top
        right = 0
        left = 0
        for i in range(height):
            right += max(grid[i])
        for i in range(width):
            left += max([ grid[j][i] for j in range(height)])
        return left + right + top
