"""
1970. Last Day Where You Can Still Cross
Hard

367

6

Add to List

Share
There is a 1-based binary matrix where 0 represents land and 1 represents water. You are given integers row and col representing the number of rows and columns in the matrix, respectively.

Initially on day 0, the entire matrix is land. However, each day a new cell becomes flooded with water. You are given a 1-based 2D array cells, where cells[i] = [ri, ci] represents that on the ith day, the cell on the rith row and cith column (1-based coordinates) will be covered with water (i.e., changed to 1).

You want to find the last day that it is possible to walk from the top to the bottom by only walking on land cells. You can start from any cell in the top row and end at any cell in the bottom row. You can only travel in the four cardinal directions (left, right, up, and down).

Return the last day where it is possible to walk from the top to the bottom by only walking on land cells.

 

Example 1:


Input: row = 2, col = 2, cells = [[1,1],[2,1],[1,2],[2,2]]
Output: 2
Explanation: The above image depicts how the matrix changes each day starting from day 0.
The last day where it is possible to cross from top to bottom is on day 2.
Example 2:


Input: row = 2, col = 2, cells = [[1,1],[1,2],[2,1],[2,2]]
Output: 1
Explanation: The above image depicts how the matrix changes each day starting from day 0.
The last day where it is possible to cross from top to bottom is on day 1.
Example 3:


Input: row = 3, col = 3, cells = [[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]]
Output: 3
Explanation: The above image depicts how the matrix changes each day starting from day 0.
The last day where it is possible to cross from top to bottom is on day 3.
 

Constraints:

2 <= row, col <= 2 * 104
4 <= row * col <= 2 * 104
cells.length == row * col
1 <= ri <= row
1 <= ci <= col
All the values of cells are unique.
Accepted
7,319
Submissions
15,206
"""
class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:

        def get_array(d): 
            arr = [ [0] * col for i in range(row)]
            for i in range(d):
                arr[cells[i][0] - 1][cells[i][1] - 1] = 1
            return arr

        def can_cross(arr, r, c, visited):
            key = (r,c)
            if key in visited:
                return False
            visited.add(key)

            if c == col or c < 0 or r < 0:
                return False
            elif r == row:
                return True
            elif arr[r][c] == 1:
                if r > 0:
                    return False
                else:
                    return can_cross(arr, r, c + 1, visited)

            if can_cross(arr, r + 1, c, visited) or can_cross(arr, r, c - 1, visited) or can_cross(arr, r, c + 1, visited) or can_cross(arr, r - 1, c, visited):
                return True
            else:
                return False
        
        #binary search
        low = 0
        high = len(cells)
        
        while high > low:
            mid = int((high + low) / 2)
            arr = get_array(mid)
            res = can_cross(arr, 0, 0, set())
            
            if res:
                low = mid + 1
            else:
                high = mid
        return high - 1
