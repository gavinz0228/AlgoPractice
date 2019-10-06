class MapSum(object):
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tree = {}
        
    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        if not key:
            return
        last = None
        if key[0] not in self.tree:
            self.tree[key[0]] = {}
        last = self.tree[key[0]]
        
        for i in range(1, len(key)):
            if key[i] not in last:
                last[key[i]] = {}
            last = last[key[i]]
        
        last["END"] = val
    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        self.s = 0
        node = self.tree
        for w in prefix:
            if w not in node:
                return 0
            node = node[w]
        self.count(node)
        return self.s
    
    def count(self, node):
        for c in node.keys():
            if c == "END":
                self.s += node[c]
            else:
                self.count(node[c])
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)