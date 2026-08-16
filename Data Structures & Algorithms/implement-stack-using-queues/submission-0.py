class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        for i in range(len(self.queue)):
            if i == len(self.queue) - 1:
                return self.queue.popleft()
            self.queue.append(self.queue.popleft())

    def top(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        if not self.queue: return True
        else: return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()