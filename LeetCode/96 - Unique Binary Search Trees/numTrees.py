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

"""
#recursion with memorization
class Solution:
    def numTrees(self, n: int) -> int:
        mem = {0:1, 1:1}
        def recursion(num):
            if num in mem:
                return mem[num]
            if num == 1 or num == 0:
                return 1
            res = 0
            for i in range(num):
                res += recursion(i) * recursion(num - i - 1)
            mem[num] = res
            return res
        return recursion(n)
            
"""
#dp derived from the above
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1,1]
        for i in range(2, n + 1):
            dp.append(sum([ dp[j] * dp[i - j - 1] for j in range(i)]))
        return dp[-1]

            
