class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(0, len(stones)):
            stones[i] = -stones[i]
        
        heapq.heapify(stones)

        while len(stones) > 1:
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)

            if stone1 == stone2: continue

            if stone1 > stone2:
                heapq.heappush(stones, stone2 - stone1)
            elif stone1 < stone2:
                heapq.heappush(stones, stone1 - stone2)
        
        if stones:
            return -stones[0]
        else:
            return 0

