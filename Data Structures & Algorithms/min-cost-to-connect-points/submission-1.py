class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        pq = []
        connected = set()
        def findNeighborsAndPush(pointIndex):
            for i in range(0, len(points)):
                if i in connected: continue
                distance = abs(points[pointIndex][0] - points[i][0]) + abs(points[pointIndex][1] - points[i][1])
                heapq.heappush(pq, (distance, i))
        
        connected.add(0)
        findNeighborsAndPush(0)
        
        edges = 0
        res = 0
        while edges < len(points) - 1:
            distance, pointIndex = heapq.heappop(pq)
            if pointIndex in connected: continue
            edges += 1
            res += distance
            connected.add(pointIndex)
            findNeighborsAndPush(pointIndex)

        return res
