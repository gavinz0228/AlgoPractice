class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        count = 0
        first2 = {}
        for i, x in enumerate(A):
            for j, y in enumerate(B):
                key = x + y
                if key in first2:
                    first2[key] += 1
                else:
                    first2[key] = 1
        for i, x in enumerate(C):
            for j, y in enumerate(D):
                target = 0 - x - y
                if target in first2:
                    count += first2[target]
        return count
                
                
        
