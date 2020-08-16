class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], x[0]) )
        l = len(intervals)
        if l == 1:
            return 0
        sol = 0
        prev = 0
        for i in range(1, l):
            if intervals[i][0] < intervals[prev][1]:
                sol += 1
            else:
                prev = i
        return sol
                
            
