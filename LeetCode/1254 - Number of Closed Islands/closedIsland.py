'''
1254. Number of Closed Islands
Medium

944

27

Add to List

Share
Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.

 

Example 1:



Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation: 
Islands in gray are closed because they are completely surrounded by water (group of 1s).
Example 2:



Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
Output: 1
Example 3:

Input: grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
Output: 2
 

Constraints:

1 <= grid.length, grid[0].length <= 100
0 <= grid[i][j] <=1
Accepted
50,581
Submissions
81,350
'''
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])
        visited = set()
        ans = 0

        def check(r, c):
            visited.add((r,c,))
            if r > height - 1 or r < 0 or c > width - 1 or c < 0:
                return False
            elif grid[r][c] == 1:
                return True
            up, down, left, right = True, True, True, True
            
            if (r + 1, c) not in visited:
                up = check(r + 1, c)
            if (r - 1, c) not in visited:
                down = check(r - 1, c)
            if (r, c + 1) not in visited:
                right = check(r, c + 1)
            if (r, c - 1) not in visited:
                left = check(r, c - 1)

            return up and down and left and right
        
        for row in range(1, height - 1):
            for col in range(1, width - 1):
                if (row,col,) not in visited:
                    if grid[row][col] == 0:
                        if check(row, col):
                            ans += 1
                           
        return ans
                