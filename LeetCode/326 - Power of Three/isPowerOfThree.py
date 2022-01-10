"""
326. Power of Three
Easy

660

87

Add to List

Share
Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.

 

Example 1:

Input: n = 27
Output: true
Example 2:

Input: n = 0
Output: false
Example 3:

Input: n = 9
Output: true
 

Constraints:

-231 <= n <= 231 - 1
 

Follow up: Could you solve it without loops/recursion?
Accepted
421,761
Submissions
978,462
"""

"""
#original solution
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0 :
            return False
        
        while n > 1:
            if n % 3 != 0:
                return False
            else:
                n = n / 3
        return True
            
"""

# this uses builtin log function
import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0 :
            return False
        res = math.log(n,3)
        return math.ceil(res) - res < 0.00000000000001
