"""
120. Triangle
Medium

4117

364

Add to List

Share
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

 

Example 1:

Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
Example 2:

Input: triangle = [[-10]]
Output: -10
 

Constraints:

1 <= triangle.length <= 200
triangle[0].length == 1
triangle[i].length == triangle[i - 1].length + 1
-104 <= triangle[i][j] <= 104
 

Follow up: Could you do this using only O(n) extra space, where n is the total number of rows in the triangle?
Accepted
370,053
Submissions
751,298
"""

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        height = len(triangle)
        if height == 0:
            return 0
        elif height == 1:
            return triangle[0][0]
        
        for i in range(height - 2, -1, -1):
            for j in range(len(triangle[i])):
                left_path = triangle[i][j] + triangle[i + 1][j]
                right_path = triangle[i][j] + triangle[i + 1][j + 1]
                triangle[i][j] = left_path if left_path < right_path else right_path
        return triangle[0][0]
