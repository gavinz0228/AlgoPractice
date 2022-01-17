"""
20. Valid Parentheses
Easy

10702

441

Add to List

Share
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
Accepted
1,893,131
Submissions
4,665,165
"""
class Solution:
    def isValid(self, s: str) -> bool:
        lookup = {")": "(", "]": "[", "}": "{" }
        left = set(["(", "[", "{"])
        stack = []
        for c in s:
            if c in left:
                stack.append(c)
            else:
                if not stack:
                    return False
                if stack[-1] != lookup[c]:
                    return False
                stack.pop()
        return len(stack) == 0
        
                
