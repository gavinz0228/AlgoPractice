class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        len_a = len(A)
        if len_a != len(B):
            return False
        if A == B:
            return len(set(A)) < len_a
        diff = []
        for i in range(len_a):
            if A[i] != B[i]:
                diff.append(i)
        if len(diff) != 2:
            return False
        la = list(A)
        la[diff[0]], la[diff[1]] = la[diff[1]], la[diff[0]]
        return "".join(la) == B
