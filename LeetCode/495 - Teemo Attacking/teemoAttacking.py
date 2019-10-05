class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        cur_max = -1
        count = 0
        for t in timeSeries:
            if t > cur_max:
                cur_max = t - 1
            extra = t + duration - 1 - cur_max
            
            if extra > 0:
                count += extra
                cur_max = t + duration - 1
        print(cur_max)
        return count
