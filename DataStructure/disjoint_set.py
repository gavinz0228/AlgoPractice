class DisjointSet:
    def __init__(self, members):
        self.members = members
        self.size = len(members)
        self.map = { m:m for m in members}
        self.num_groups = self.size

    def union(self, x, y):
       xroot, yroot = self.find(x), self.find(y)
       if xroot != yroot:
           self.map[x] = y
           self.num_groups -= 1
    def find(self, x):
        while x != self.map[x]:
            x = self.map[x]
        return x
    def get_groups(self):
        visited = set()
        groups = {}
        for m in members:
            if m not in visited:
                went_thru = [m]
                cur = m
                while cur != self.map[cur]:
                    cur = self.map[cur]
                    went_thru.append(cur)
                visited.update(went_thru)
                if cur not in groups:
                    groups[cur] = []
                groups[cur].extend(went_thru)
        return groups
