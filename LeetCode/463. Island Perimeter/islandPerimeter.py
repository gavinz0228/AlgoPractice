"""
463. Island Perimeter
Easy

3999

224

Add to List

Share
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

Example 1:


Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.
Example 2:

Input: grid = [[1]]
Output: 4
Example 3:

Input: grid = [[1,0]]
Output: 4
 

Constraints:

row == grid.length
col == grid[i].length
1 <= row, col <= 100
grid[i][j] is 0 or 1.
There is exactly one island in grid.
Accepted
344,632
Submissions
501,949
"""
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        height = len(grid)
        width = len(grid[0])
        perimeter = 0
        for r in range(height):
            for c in range(width):
                if grid[r][c] == 1:
                    perimeter += 4
                    if r >= 1 and grid[r - 1][c] == 1:
                        perimeter -= 1
                    if c >= 1 and grid[r][c - 1] == 1:
                        perimeter -= 1
                    if r < height - 1 and grid[r + 1][c] == 1:
                        perimeter -= 1
                    if c < width - 1 and grid[r][c + 1] == 1:
                        perimeter -= 1
        return perimeter
