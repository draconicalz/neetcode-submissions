class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []

        for point in points:
            heapq.heappush(pq, ((point[0]**2 + point[1]**2)**(1/2) , point))
        
        res = []
        for _ in range(0, k):
            dist, point = heapq.heappop(pq)
            res.append(point)
        
        return res