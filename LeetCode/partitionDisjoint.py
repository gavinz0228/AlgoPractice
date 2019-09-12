class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        length = len(A)
        minn = A[-1]
        dp = [minn]
        for i in range(length - 2, -1, -1):
            if A[i] < minn:
                minn = A[i]
            dp.insert(0, minn)
        count = 1
        maxn = A[0]
        for i in range(1, length):
            if maxn <= dp[i]:
                break
            if A[i] > maxn:
                maxn = A[i]
            count += 1
        return count
