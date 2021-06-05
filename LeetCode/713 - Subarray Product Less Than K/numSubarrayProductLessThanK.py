'''
713. Subarray Product Less Than K
Medium

2406

90

Add to List

Share
Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

 

Example 1:

Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
Example 2:

Input: nums = [1,2,3], k = 0
Output: 0
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] < 1000
0 <= k < 106
Accepted
105,557
Submissions
259,357
'''
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        sol= 0
        slow = 0
        cur = 1
        for fast,val in enumerate(nums):
            cur *= val
            while cur >= k:
                cur /= nums[slow]
                slow += 1
            sol += fast - slow + 1

        return sol
