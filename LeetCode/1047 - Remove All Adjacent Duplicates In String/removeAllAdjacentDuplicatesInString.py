class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        stack = []
        for x in S:
            if not stack or stack[-1] != x:
                stack.append(x)
            else:
                while stack and stack[-1] == x:
                    stack.pop()
        return "".join(stack)