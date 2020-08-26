class Node:
    prv = None
    nxt = None
    key = None
    val = None
    def __init__(self, key, val, prv, nxt):
        self.prv = prv
        self.nxt = nxt
        self.val = val
        self.key = key
        
class LRUCache:

    def __init__(self, capacity: int):
        self.list_head = Node(None,None,None,None)
        self.list_tail = Node(None,None,self.list_head,None)
        self.list_head.nxt = self.list_tail
        self.count = 0
        self.dict = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.dict:
            node = self.dict[key]
            self.moveToHead(node)
            return node.val
        else:
            return -1
    
    def moveToHead(self, node):
        #remove it from middle
        prev_node = node.prv
        next_node = node.nxt
        prev_node.nxt = next_node
        next_node.prv = prev_node
        cur_first = self.list_head.nxt
        self.list_head.nxt = node
        node.prv = self.list_head
        node.nxt = cur_first
        cur_first.prv = node

    def deleteLast(self):
        cur_last = self.list_tail.prv
        last_second = cur_last.prv
        last_second.nxt = self.list_tail
        self.list_tail.prv = last_second
        del self.dict[cur_last.key]
        self.count -= 1

    def addToHead(self, key, value):
        cur_first = self.list_head.nxt
        self.list_head.nxt = Node(key, value, self.list_head, cur_first)
        self.dict[key] = self.list_head.nxt
        cur_first.prv = self.list_head.nxt
        self.count += 1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            node = self.dict[key]
            node.val = value
            self.moveToHead(node)
        else:
            self.addToHead(key, value)
            if self.count > self.capacity:
                self.deleteLast()
