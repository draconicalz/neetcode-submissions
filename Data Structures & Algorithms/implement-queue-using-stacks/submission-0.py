class MyQueue:

    def __init__(self):
        self.s = []

    def push(self, x: int) -> None:
        arr = []
        while self.s:
            arr.append(self.s.pop())
        self.s = [x] + arr[::-1]


    def pop(self) -> int:
        return self.s.pop()
        

    def peek(self) -> int:
        return self.s[-1]

    def empty(self) -> bool:
        return False if self.s else True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()