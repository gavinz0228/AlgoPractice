"""342. Power of Four
Easy

1245

276

Add to List

Share
Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.

 

Example 1:

Input: n = 16
Output: true
Example 2:

Input: n = 5
Output: false
Example 3:

Input: n = 1
Output: true
 

Constraints:

-231 <= n <= 231 - 1
 

Follow up: Could you solve it without loops/recursion?
Accepted
270,069
Submissions
624,611
"""
import math
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0 :
            return False
        
        while n > 1:
            if n % 4 != 0:
                return False
            else:
                n = n / 4
        return True
