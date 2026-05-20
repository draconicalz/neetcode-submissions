class MedianFinder:

    def __init__(self):
        # Using max heap so biggest num at 0 (push with negative)
        self.left = []
        # Using min heap so smallest num at 0
        self.right = []

    def addNum(self, num: int) -> None:
        if self.right and num > self.right[0]:
            heapq.heappush(self.right, num)
        else:
            heapq.heappush(self.left, -num)
        
        if len(self.left) > len(self.right):
            to_push = heapq.heappop(self.left)
            heapq.heappush(self.right, -to_push)
        elif len(self.left) < len(self.right):
            to_push = heapq.heappop(self.right)
            heapq.heappush(self.left, -to_push)


    def findMedian(self) -> float:
        if len(self.right) > len(self.left):
            return self.right[0]
        elif len(self.right) < len(self.left):
            return -self.left[0]
        else:
            return (self.right[0] + -self.left[0]) / 2
        