class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        length = len(pushed)
        stack = []
        popidx = 0
        pushidx = 0
        while popidx < length :
            if stack and stack[-1] == popped[popidx]:
                popidx += 1
                stack.pop()
                continue
            found = False
            for i in range(pushidx, length):
                if pushed[i] != popped[popidx]:
                    stack.append(pushed[i])
                    pushidx += 1
                else:
                    found = True
                    pushidx += 1
                    popidx += 1
                    break
            if not found:
                return False
        return True
                
print(Solution().validateStackSequences([1,0,2],[2,1,0]))