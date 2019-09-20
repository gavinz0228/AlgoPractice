class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort(reverse=True)
        for i in range(len(A) - 2):
            a, b, c = A[i: i + 3]
            if b + c > a:
                return a + b + c
        return 0
