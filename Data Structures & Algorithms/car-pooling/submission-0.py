class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # sort by trip start time
        trips.sort(key = lambda x: x[1])

        pq = []
        curPass = 0
        for t in trips:
            numPass, start, end = t
            while pq and pq[0][0] <= start:
                curPass -= pq[0][1]
                heapq.heappop(pq)

            curPass += numPass
            if curPass > capacity:
                return False
            heapq.heappush(pq, [end, numPass])
        return True