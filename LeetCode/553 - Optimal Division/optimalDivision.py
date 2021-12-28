"""
553. Optimal Division
Medium

239

1325

Add to List

Share
You are given an integer array nums. The adjacent integers in nums will perform the float division.

For example, for nums = [2,3,4], we will evaluate the expression "2/3/4".
However, you can add any number of parenthesis at any position to change the priority of operations. You want to add these parentheses such the value of the expression after the evaluation is maximum.

Return the corresponding expression that has the maximum value in string format.

Note: your expression should not contain redundant parenthesis.

 

Example 1:

Input: nums = [1000,100,10,2]
Output: "1000/(100/10/2)"
Explanation:
1000/(100/10/2) = 1000/((100/10)/2) = 200
However, the bold parenthesis in "1000/((100/10)/2)" are redundant, since they don't influence the operation priority. So you should return "1000/(100/10/2)".
Other cases:
1000/(100/10)/2 = 50
1000/(100/(10/2)) = 50
1000/100/10/2 = 0.5
1000/100/(10/2) = 2
Example 2:

Input: nums = [2,3,4]
Output: "2/(3/4)"
Example 3:

Input: nums = [2]
Output: "2"
 

Constraints:

1 <= nums.length <= 10
2 <= nums[i] <= 1000
There is only one optimal division for the given iput.
Accepted
30,243
Submissions
51,688
"""

"""class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        l = len(nums)
        max_dp = {}
        min_dp = {}
        max_dp_sol = {}
        min_dp_sol = {}
        def helper(start, end):            
            key = (start, end,)

            if key in max_dp:
                return max_dp[key], min_dp[key], max_dp_sol[key], min_dp_sol[key]
            
            if start == end:
        
                max_dp[key] = nums[start]
                min_dp[key] = nums[start]
                max_dp_sol[key] = [str(nums[start])]
                min_dp_sol[key] = [str(nums[start])]
                return max_dp[key], min_dp[key], max_dp_sol[key], min_dp_sol[key]

            max_val = float('-inf')
            min_val = float('inf')
            max_sol = None
            min_sol = None
            for i in range(start, end):
                left_max, left_min, left_max_str, left_min_str = helper(start, i)
                right_max, right_min, right_max_str, right_min_str = helper(i + 1, end)
                if left_max / right_min > max_val:
                    max_val = left_max / right_min
                    if len(right_min_str) > 1:
                        max_sol = left_max_str + ["/", "("] + right_min_str + [")"]
                    else:
                        max_sol = left_max_str + ["/"] + right_min_str
                if left_min / right_max < min_val:
                    min_val = left_min / right_max
                    if len(right_max_str) > 1:
                        min_sol = left_min_str + ["/", "("] + right_max_str + [")"]
                    else:
                        min_sol = left_min_str + ["/"] + right_max_str

            max_dp[key] = max_val
            min_dp[key] = min_val
            max_dp_sol[key] = max_sol
            min_dp_sol[key] = min_sol
            return max_val, min_val, max_sol, min_sol
        _, _, sol, _ = helper(0, l - 1)
        return "".join(sol)
"""

class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        l = len(nums)
        if l == 1:
            return str(nums[0])
        elif l == 2:
            return str(nums[0]) + '/' + str(nums[1])
        sol = [str(nums[0]), '/', '(', str(nums[1]) ]
        for i in range(2, l):
            sol.append('/')
            sol.append(str(nums[i]))
        sol.append(")")
        return "".join(sol)
