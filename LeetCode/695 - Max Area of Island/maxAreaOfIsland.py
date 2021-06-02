'''
695. Max Area of Island
Medium

3515

111

Add to List

Share
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

 

Example 1:


Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.
Accepted
275,346
Submissions
413,367
'''

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.visited = set()
        self.height = len(grid)
        self.width =  len(grid[0])
        self.grid = grid
        curr_max = 0
        for r in range(self.height):
            for c in range(self.width):
                if (r,c,) not in self.visited:
                    if grid[r][c] == 1:
                        curr = self.examine(r,c)
                        curr_max = max(curr_max, curr)
        return curr_max
    def examine(self, r, c):
        if r >= self.height or r < 0 or c >= self.width or c < 0 or (r,c,) in self.visited:
            return 0
        self.visited.add((r,c,))
        if self.grid[r][c] == 0:
            return 0
        
        return 1 + self.examine(r+1,c) + self.examine(r-1,c) + self.examine(r,c+1) + self.examine(r,c-1)
