class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        length = len(pushed)
        popidx = 0
        left, right = 0, 0
        while popidx < length:
            for  


                
print(Solution().validateStackSequences([1,0,2],[2,1,0]))