class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        maxheap = []
        for gift in gifts:
            heapq.heappush(maxheap, -gift)
        
        for _ in range(k):
            cur = heapq.heappop(maxheap)
            heapq.heappush(maxheap, -int(sqrt(-cur)))
        res = 0
        for gift in maxheap:
            res -= gift
        return res