from typing import List

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        p = self.getPattern(pattern)
        
        res = []
        for w in words:
            if self.getPattern(w) == p:
                res.append(w)
        return res
        
    def getPattern(self, words):
        i = 0
        lookup = {}
        res = []
        for w in words:
            if w in lookup:
                res.append(lookup[w])
            else:
                lookup[w] = i
                res.append(i)
                i += 1
        return tuple(res)