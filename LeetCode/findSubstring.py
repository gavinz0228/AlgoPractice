class Solution(object):
    def check(self, s, words, wl):
        ss = {}
        for w in words:
            if w in ss:
                ss[w] = ss[w] + 1
            else:
                ss[w] = 1
        idx = 0
        eidx = len(s) 
        while idx < eidx:
            curr = s[idx: idx + wl]
            if curr in ss:
                if ss[curr] == 1:
                    del ss[curr]
                else:
                    ss[curr] = ss[curr] - 1
                idx += wl
            else:
                return False
        if len(ss) == 0:
            return True
        
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []
        sol = []
        l = len(s)
        wl = len(words[0])
        vol = wl * len(words)
        if vol == 0 :
            return []
        offset = l - vol
        if vol == 0:
            return []

        for o in range(offset + 1):
            if self.check(s[o:o + vol], words, wl):
                sol.append(o)
        return sol
