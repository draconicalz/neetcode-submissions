class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        pq = []
        for i, height in enumerate(heights):
            while pq and pq[0][0] <= height:
                heapq.heappop(pq)
            heapq.heappush(pq, [height, i])
        res = []
        for height, i in pq:
            res.append(i)
        return sorted(res)
