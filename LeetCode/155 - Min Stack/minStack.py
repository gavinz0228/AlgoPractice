from heapq import heappop, heappush
from collections import defaultdict
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.mins = []
        self.nums = []
        self.count = defaultdict(int)

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """

        self.count[x] += 1
        self.nums.append(x)
        heappush(self.mins, x)
        

    def pop(self):
        """
        :rtype: None
        """
        cur = self.nums.pop()
        while self.count[cur] == 0:
            cur = self.nums.pop()
        self.count[cur] -= 1
        return cur

    def top(self):
        """
        :rtype: int
        """
        cur = self.nums[-1]
        while self.count[cur] == 0:
            cur = self.nums.pop()
        return cur

    def getMin(self):
        """
        :rtype: int
        """
        cur = self.mins[0]
        while self.count[cur] == 0:
            heappop(self.mins)
            cur = self.mins[0]
        return cur
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()