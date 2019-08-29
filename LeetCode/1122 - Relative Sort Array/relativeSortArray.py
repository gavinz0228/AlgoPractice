from collections import Counter
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = Counter(arr1)
        res = []
        for x in arr2:
            res.extend([x]*count[x])
            del count[x]
        keys = sorted(count.keys())
        for k in keys:
            res.extend([k]*count[k])
            del count[k] 
        return res