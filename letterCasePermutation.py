class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        length = len(S)
        sol = [ [f] for f in self.getForms(S[0]) ]
        for i in range(1, length):
            forms = self.getForms(S[i])
            if len(forms) == 1:
                for s in sol:
                    s.append(forms[0])
            else:
                new = []
                for s in sol:
                    new.append(s + [forms[0]])
                    s.append(forms[1])
                sol.extend(new)

        return [ "".join(s) for s in sol]
    def getForms(self, c):
        res = []
        n = ord(c)
        res.append(c)
        if n >= 48 and n<= 57:
            pass
        elif n >= 97:
            res.append(chr(n-32))
        else:
            res.append(chr(n+32))
        return res
        
