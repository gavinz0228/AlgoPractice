'''
394. Decode String
Medium

5183

244

Add to List

Share
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
Example 4:

Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"
 

Constraints:

1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].
Accepted
335,602
Submissions
627,726
'''
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c != ']':
                stack.append(c)
            else:
                temp = []
                while True:
                    c = stack.pop()
                    if c == '[':
                        break
                    temp.append(c)
                number = []
                while stack and stack[-1].isnumeric():
                    number.append(stack.pop())
                #repeat it
                n = int("".join(number[::-1]))
                curr = ''.join([''.join(temp)] * n)
                #push it back to stack
                for x in curr[::-1]:
                    stack.append(x)
        return ''.join(stack)
    def repeat(self, s, n):
        return 
