class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        newspan = 1
        while self.stack and self.stack[-1][0] <= price:
            oldprice, oldspan = self.stack.pop()
            newspan += oldspan
        
        self.stack.append((price, newspan))
        return newspan

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)