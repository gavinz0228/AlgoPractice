class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        self.length = len(rooms)
        self.rooms = rooms
        visited = set()
        self.search(0, visited)
        if self.length == len(visited):
            return True

    def search(self, i, visited):
        if self.length == i:
            return
        if i not in visited:
            visited.add(i)
            for nxt in self.rooms[i]:
                self.search(nxt, visited)
