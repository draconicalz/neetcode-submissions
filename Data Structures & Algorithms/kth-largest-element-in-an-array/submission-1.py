class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        for num in nums:
            heapq.heappush(pq, -num)
        
        res = []
        for _ in range(0, k):
            res = heapq.heappop(pq)
        return -res

