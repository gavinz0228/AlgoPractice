from collections import deque
class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        if not T:
            return []
        length = len(T)
        result = deque([0])
        stack = [(T[-1],length-1) ]
        for i in range(length -2, -1, -1):
            if T[i] < stack[-1][0]:
                result.appendleft(1)
            else:
                last = stack.pop()
                while last[0] <= T[i] and stack:
                    last = stack.pop()

                if last[0] <= T[i]:
                    result.appendleft(0)
                else:
                    stack.append(last)
                    result.appendleft(last[1] - i)
            stack.append((T[i],i) )
        return result