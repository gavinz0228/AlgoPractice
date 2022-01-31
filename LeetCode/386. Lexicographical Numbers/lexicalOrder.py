"""
386. Lexicographical Numbers
Medium

1081

109

Add to List

Share
Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.

You must write an algorithm that runs in O(n) time and uses O(1) extra space. 

 

Example 1:

Input: n = 13
Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]
Example 2:

Input: n = 2
Output: [1,2]
 

Constraints:

1 <= n <= 5 * 104
Accepted
78,386
Submissions
135,238
"""
class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        def add(res, base, limit):
            base = base * 10
            if base <= limit:
                res.append(base)
                add(res, base, limit)
                curr = base + 1
                curr_limit = min(base + 9, limit)
                while curr <= curr_limit:
                    res.append(curr)
                    add(res, curr, limit)
                    curr +=1
        for i in range(1, min(10, n + 1)):
            res.append(i)
            add(res, i, n)
        return res
