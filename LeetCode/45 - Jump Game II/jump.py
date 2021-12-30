"""
45. Jump Game II
Medium

6652

255

Add to List

Share
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 1000
Accepted
504,410
Submissions
1,410,359
"""

"""class Solution:
    def jump(self, nums: List[int]) -> int:
        length = len(nums)
        dp = [float('inf')] * length
        dp[0] = 0
        for i in range(length):
            for j in range(nums[i]):
                if i + j + 1 < length and i + 1 < length:
                    dp[i + j + 1] = min(dp[i + j + 1], dp[i] + 1)
        return dp[-1]
"""

class Solution:
    def jump(self, nums: List[int]) -> int:
        l = 0
        r = 0
        jump = 0
        length = len(nums)
        right_most = 0
        while r < length - 1:
            for i in range(l, r + 1):
                right_most = max(nums[i] + i, right_most)
                
            l = r + 1
            r = right_most
            jump += 1
        return jump

