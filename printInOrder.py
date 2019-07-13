import threading
class Foo:
    def __init__(self):
        self.lock = threading.Lock()
        self.stage = 1
    def acquire(self, n):
        self.lock.acquire()
        if self.stage == n:
            return True
        else:
            self.lock.release()
    def release(self):
        self.stage += 1
        self.lock.release()
                
    def first(self, printFirst: 'Callable[[], None]') -> None:
        while not self.acquire(1): pass
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.release()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        while not self.acquire(2): pass
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.release()


    def third(self, printThird: 'Callable[[], None]') -> None:

        while not self.acquire(3): pass
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
        self.release()
