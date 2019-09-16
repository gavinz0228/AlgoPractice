

class Solution:
    def __init__(self):
        self.lookup = {x: 1 for x in "qwertyuiop"}
        self.lookup.update({x: 2 for x in "asdfghjkl"})
        self.lookup.update({x: 3 for x in "zxcvbnm"})

    def findWords(self, words: List[str]) -> List[str]:
        res = []
        for w in words:
            if len(set([self.lookup[c] for c in w.lower()])) == 1:
                res.append(w)
        return res
