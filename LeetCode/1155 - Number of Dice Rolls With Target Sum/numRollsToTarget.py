'''
1155. Number of Dice Rolls With Target Sum
Medium

1388

64

Add to List

Share
You have d dice and each die has f faces numbered 1, 2, ..., f.

Return the number of possible ways (out of fd total ways) modulo 109 + 7 to roll the dice so the sum of the face-up numbers equals target.

 

Example 1:

Input: d = 1, f = 6, target = 3
Output: 1
Explanation: 
You throw one die with 6 faces.  There is only one way to get a sum of 3.
Example 2:

Input: d = 2, f = 6, target = 7
Output: 6
Explanation: 
You throw two dice, each with 6 faces.  There are 6 ways to get a sum of 7:
1+6, 2+5, 3+4, 4+3, 5+2, 6+1.
Example 3:

Input: d = 2, f = 5, target = 10
Output: 1
Explanation: 
You throw two dice, each with 5 faces.  There is only one way to get a sum of 10: 5+5.
Example 4:

Input: d = 1, f = 2, target = 3
Output: 0
Explanation: 
You throw one die with 2 faces.  There is no way to get a sum of 3.
Example 5:

Input: d = 30, f = 30, target = 500
Output: 222616187
Explanation: 
The answer must be returned modulo 10^9 + 7.
 

Constraints:

1 <= d, f <= 30
1 <= target <= 1000
Accepted
75,716
Submissions
158,685
'''
class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        MOD = 10**9 + 7
        cache = {}
        def find(num, face, tar):
            #print((num, face, tar))
            if tar < num:
                return 0
            elif num == 1:
                return 1 if tar <= face else 0

            cache_key = (num, face, tar,)
            if cache_key not in cache:
                
                curr_sum = 0
                for i in range(1, face + 1):
                    curr_sum += find(num - 1, face, tar - i)
                    curr_sum = curr_sum % MOD
                cache[cache_key] = curr_sum
            return cache[cache_key]
        
        return find(d, f, target)