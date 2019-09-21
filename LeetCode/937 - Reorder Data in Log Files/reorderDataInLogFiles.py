from collections import deque


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        q = deque([])
        alpha = []
        for x in logs:
            parts = x.split()
            identifier, log = parts[0], parts[1:]
            if all([l.isdigit() for l in log]):
                q.append(x)
            else:
                alpha.append((" ".join(log), identifier))
        alpha.sort(reverse=True)
        for a in alpha:
            q.appendleft(a[1] + " " + a[0])
        return q
