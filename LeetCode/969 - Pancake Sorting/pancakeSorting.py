class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        sol = []
        length = len(A)
        for i in range(length - 1, 0, -1):
            maxp = (A[0], 0)
            inorder = True
            for j in range(1, i+1):
                if A[j] > maxp[0]:
                    maxp = (A[j], j)
                if A[j] < A[j - 1]:
                    inorder = False
            if inorder:
                return sol
            A[: maxp[1] + 1] = A[: maxp[1] + 1][::-1]
            A[:i+1] = A[:i+1][::-1]
            sol.append(maxp[1] + 1)
            sol.append(i + 1)
        return sol
