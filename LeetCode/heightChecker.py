from bisect import bisect
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        lst = []
        count = 0
        for x in heights:
            i = bisect(lst, x)
            lst.insert(i, x)
        for i, x in enumerate(heights):
            if lst[i] != x:
                count += 1
        return count
        
