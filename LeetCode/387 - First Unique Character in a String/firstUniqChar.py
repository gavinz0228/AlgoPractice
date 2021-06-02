'''
Given a string s, return the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1
 

Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.
Accepted
750,726
Submissions
1,381,540
'''
from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count_lookup = Counter(s)
        for i in range(len(s)):
            if count_lookup[s[i]] == 1:
                return i
        return -1
