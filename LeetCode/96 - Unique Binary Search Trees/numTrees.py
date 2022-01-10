"""
96. Unique Binary Search Trees
Medium

6472

255

Add to List

Share
Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

 

Example 1:


Input: n = 3
Output: 5
Example 2:

Input: n = 1
Output: 1
 

Constraints:

1 <= n <= 19
"""
class Solution:
    def numTrees(self, n: int) -> int:
        def recursion(num):
            if num == 1 or num == 0:
                return 1
            res = 0
            for i in range(num):
                res += recursion(i) * recursion(num - i - 1)

            return res
        return recursion(n)
            
