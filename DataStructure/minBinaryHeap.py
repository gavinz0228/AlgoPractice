class Heap:
    def __init__(self):
        self.heap_arr = []
    def push(self, value):
        last_idx = len(self.heap_arr)
        self.heap_arr.append(value)
        cur = last_idx
        target = (cur - 1) / 2
        while target > -1 and self.heap_arr[cur] < self.heap_arr[target]:
            self.heap_arr[cur], self.heap_arr[target] = self.heap_arr[target], self.heap_arr[cur]
            cur = target
            target =  (cur - 1) / 2

    def pop(self):
        if not self.heap_arr:
            return
        elif len(self.heap_arr) == 1:
            return self.heap_arr.pop()
        last = self.heap_arr.pop()
        res = self.heap_arr[0]
        self.heap_arr[0] = last
        length = len(self.heap_arr)
        cur = 0
        while True:
            left, right = cur * 2 + 1, cur * 2 + 2
            smaller_child = None
            if left < length:
                if self.heap_arr[cur] > self.heap_arr[left]:
                    smaller_child = left
            if right < length:
                if not smaller_child:
                    if self.heap_arr[cur] > self.heap_arr[right]:
                        smaller_child = right
                elif self.heap_arr[smaller_child] > self.heap_arr[right]:
                    smaller_child = right
            if smaller_child:
                self.heap_arr[cur], self.heap_arr[smaller_child] = self.heap_arr[smaller_child], self.heap_arr[cur]
            if not smaller_child:
                break
            cur = smaller_child
        return res

    def is_empty(self):
        return not self.heap_arr

h = Heap()
arr = [1,9,3,2,70,5,6,3,9,7]
for x in arr:
    h.push(x)
print(h.heap_arr)
print("--")
while not h.is_empty():
    print(h.pop())