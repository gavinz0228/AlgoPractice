class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        s = sum(A)
        if s % 3 != 0:
            return False
        average = s / 3
        cur = 0
        count = 0
        for n in A:
            cur += n
            if cur == average:
                cur = 0
                count += 1
        if cur == 0 and count == 3:
            return True
        else:
            return False
