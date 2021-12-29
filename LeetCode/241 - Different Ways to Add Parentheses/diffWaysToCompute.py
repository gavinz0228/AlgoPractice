"""
241. Different Ways to Add Parentheses
Medium

3068

157

Add to List

Share
Given a string expression of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. You may return the answer in any order.

 

Example 1:

Input: expression = "2-1-1"
Output: [0,2]
Explanation:
((2-1)-1) = 0 
(2-(1-1)) = 2
Example 2:

Input: expression = "2*3-4*5"
Output: [-34,-14,-10,-10,10]
Explanation:
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10
 

Constraints:

1 <= expression.length <= 20
expression consists of digits and the operator '+', '-', and '*'.
All the integer values in the input expression are in the range [0, 99].
Accepted
146,937
Submissions
243,642
"""

from collections import defaultdict
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        l = len(expression)
        def get_tokens(exp):
            ops = []
            nums = []
            num_start_idx = 0
            for i, c in enumerate(exp):
                if c in ['+', '-', '*']:
                    ops.append(c)
                    nums.append(int(exp[num_start_idx:i]))
                    num_start_idx = i + 1
                elif i == l - 1:
                    nums.append(int(exp[num_start_idx:i+1]))
            return nums, ops
        def calc(num1, op, num2):
            if op == '+':
                return num1 + num2
            elif op == '-':
                return num1 - num2
            elif op == '*':
                return num1 * num2

        nums, ops = get_tokens(expression)
        cache = {}
        def helper(start, end):
            key = (start, end,)
            if key in cache:
                return cache[key]
            nlen = end - start
            if nlen == 1:
                return [nums[start]]
            elif nlen == 2:
                return [calc(nums[start], ops[start], nums[start + 1])]
            sol = []
            num1 = nums[start]

            for i in range(start + 1, end):
                #recursion on both the left side and the right side
                for ln in helper(start, i):
                    for rn in helper(i, end):
                        sol.append( calc(ln, ops[i-1], rn) )
                num1 = calc(num1, ops[i - 1], nums[i])
            cache[key] = sol
            return sol
        return helper(0, len(nums))
                    
                    
        
