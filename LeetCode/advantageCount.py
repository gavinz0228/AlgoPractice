from bisect import bisect
class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        A.sort()
        result = []
        l = len(A)
        for x in B:
            idx = bisect(A, x)
            if idx == l:
                result.append(A[0])
                del A[0]
            else:
                result.append(A[idx])
                del A[idx]
            l -= 1
        return result
