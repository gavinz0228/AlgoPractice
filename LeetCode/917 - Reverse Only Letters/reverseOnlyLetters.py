class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        length = len(S)
        sol = []

        def aux():
            for i in range(length):
                c = S[length - i - 1]
                if c.isalpha():
                    yield c
        iterator = iter(aux())
        for x in S:
            if x.isalpha():
                sol.append(next(iterator))
            else:
                sol.append(x)
        return "".join(sol)
