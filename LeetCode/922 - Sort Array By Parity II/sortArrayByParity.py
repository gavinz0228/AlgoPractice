from typing import List


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        odd = []
        even = []
        cur, nex = even, odd
        for i, n in enumerate(A):
            if i % 2 != n % 2:
                cur.append(i)
            cur, nex = nex, cur
        for i in range(len(odd)):
            A[odd[i]], A[even[i]] = A[even[i]], A[odd[i]]
        return A
