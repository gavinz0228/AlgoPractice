class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        width = len(grid)
        rowMax = { i:max(grid[i]) for i in range(width)}
        colMax = { i:max( grid[j][i] for j in range(width)) for i in range(width)}
        sumn = 0
        for i in range(width): 
            for j in range(width):
                sumn += min(rowMax[i],colMax[j]) - grid[i][j]
        return sumn