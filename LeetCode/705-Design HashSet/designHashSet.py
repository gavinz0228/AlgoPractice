class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = [None]* 1000
        self.extend = [None]* 1000
        
    def hash(self, key):
        return key % 1000
    
    def add(self, key: int) -> None:
        h = self.hash(key)
        if self.data[h] == None:
            self.data[h] = key
        elif self.data[h] != key:
            if self.extend[h] == None:
                self.extend[h] = [key]
            else:
                if key not in self.extend[h]:
                    self.extend[h].append(key)
        
    def remove(self, key: int) -> None:
        h = self.hash(key)
        if self.data[h] != None:
            if self.data[h] == key:
                if self.extend[h] == None:
                    self.data[h] = None
                else:
                    to_move = self.extend[h].pop()
                    self.data[h] = to_move
            else:
                if self.extend[h] != None and key in self.extend[h]:
                    self.extend[h].remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        h = self.hash(key)
        if self.data[h] == None:
            return False
        else:
            if self.data[h] == key:
                return True
            else:
                if self.extend[h] != None and key in self.extend[h]:
                    return True
        
        return False
        
