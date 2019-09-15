from collections import deque


class RecentCounter:

    def __init__(self):
        self.last = deque([])

    def ping(self, t: int) -> int:
        self.last.append(t)
        min_time = t - 3000
        while self.last[0] < min_time:
            self.last.popleft()
        return len(self.last)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
