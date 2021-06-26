'''
560. Subarray Sum Equals K
Medium

7899

264

Add to List

Share
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 

Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
Accepted
506,712
Submissions
1,159,915
'''
from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0

        past_sum = defaultdict(int)
        past_sum[0] = 1
        cur_sum = 0
        sol = 0
        for i, n in enumerate(nums):
            cur_sum += n
            if cur_sum - k  in past_sum:
                sol += past_sum[cur_sum - k]
            past_sum[cur_sum] += 1
        return sol
