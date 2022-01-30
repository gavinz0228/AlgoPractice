"""
97. Interleaving String
Medium

3496

185

Add to List

Share
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.

 

Example 1:


Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
Example 3:

Input: s1 = "", s2 = "", s3 = ""
Output: true
 

Constraints:

0 <= s1.length, s2.length <= 100
0 <= s3.length <= 200
s1, s2, and s3 consist of lowercase English letters.
 

Follow up: Could you solve it using only O(s2.length) additional memory space?

Accepted
246,730
Submissions
717,497
"""
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)
        l3 = len(s3)

        if l1 + l2 != l3:
            return False
        visited = set()
        def backTrack(i1, i2, i3):
            key = (i1, i2)
            if key in visited:
                return False
            visited.add(key)
            if i1 == l1 and i2 == l2 :
                return i3 == l3
            elif i1 == l1:
                return s2[i2:] == s3[i3:]
            elif i2 == l2:
                return s1[i1:] == s3[i3:]
            else:

                left, right = i1, i3
                while left < l1 and s1[left] == s3[right] :
                    left += 1
                    right += 1
                    if(backTrack(left, i2, right )):
                        return True

                    
                left, right = i2, i3
                while left < l2 and s2[left] == s3[right]:
                    left += 1
                    right += 1
                    if(backTrack(i1, left, right)):
                        return True

                return False
        return backTrack(0,0,0)
