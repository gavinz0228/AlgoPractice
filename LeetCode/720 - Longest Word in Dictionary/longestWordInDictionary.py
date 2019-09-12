class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        if not words:
            return ""
        wl = [(len(w), w)for w in words]
        wl.sort()
        ws = set( w[1] for w in wl if w[0] == 1)
        res = [min(ws)]
        for i in range(len(ws) - 1, len(wl)):
            if wl[i][1][:-1] in ws:
                ws.add(wl[i][1])
                if not res or len(wl[i][1]) > len(res[-1])  or wl[i][1] < res[-1]:
                    res.append(wl[i][1])
        if res:
            return res[-1]