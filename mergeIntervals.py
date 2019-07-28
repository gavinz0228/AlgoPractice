class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        length = len(intervals)
        intervals.sort()
        if length <= 1:
            return intervals
        i = 0
        sol = []
        while i < length - 1:
            minn = intervals[i][0]
            maxn = intervals[i][1]
            curr = i 
            while curr < length - 1 and intervals[curr + 1][0] <= maxn:
                curr += 1
                if intervals[curr][1] > maxn:
                    maxn = intervals[curr][1]
                if intervals[curr][0] < minn:
                    minn = intervals[curr][0]
                
            if curr == i:
                sol.append(intervals[i])
                i = i + 1
            else:
                sol.append([minn, maxn])
                i = curr + 1
        if i < length:
            sol.append(intervals[i])
        return sol
