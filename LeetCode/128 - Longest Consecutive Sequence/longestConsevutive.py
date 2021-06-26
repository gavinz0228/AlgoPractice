'''
128. Longest Consecutive Sequence
Medium

5879

276

Add to List

Share
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
Accepted
453,310
Submissions
958,321
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        ans = 0
        for n in num_set:
            if n - 1 not in num_set:
                c = n
                curr = 1
                while c + 1 in num_set:
                    curr += 1
                    c += 1
                ans = max(ans, curr)
        return ans