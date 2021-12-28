"""
343. Integer Break
Medium

2333

303

Add to List

Share
Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.

Return the maximum product you can get.

 

Example 1:

Input: n = 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.
Example 2:

Input: n = 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
 

Constraints:

2 <= n <= 58
Accepted
165,853
Submissions
312,760
"""

class Solution:
    def integerBreak(self, n: int) -> int:
        minVal = float('-inf')
        dp = [minVal] * (n + 1)
        dp[1] = 1
        def helper(num):
            dpVal = dp[num]
            if dpVal != minVal:
                return dpVal
            max_val = minVal
            for i in range(1, int(num / 2) + 1):
                if num == n:
                    max_val = max(max_val, helper(num - i) * helper(i))
                else:
                    max_val = max(max_val, helper(num - i) * helper(i), num)
            dp[num] = max_val
            return max_val
        return helper(n)

        
            
