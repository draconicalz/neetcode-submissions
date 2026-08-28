class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        pq = []
        if a > 0: heapq.heappush(pq, (-a, "a"))
        if b > 0: heapq.heappush(pq, (-b, "b"))
        if c > 0: heapq.heappush(pq, (-c, "c"))
        
        
        
        combo = 0
        curl = None
        res = []
        hold = None
        while pq:
            # pop most frequent count off
            count, c = heapq.heappop(pq)

            # if we have 3 in a row, hold onto what we just popped and pop again
            # if we can't pop again, we cannot make a happy string
            if combo == 2 and curl == c:
                hold = (count, c)
                if not pq: break

                count, c = heapq.heappop(pq)
                combo = 0
                curl = None
            
            # Reset combo if we have a different character
            if curl != c: combo = 0
            combo += 1
            
            # add character to res, set cur character to c, push it back with -1 count
            res.append(c)
            curl = c
            if count + 1 < 0:
                heapq.heappush(pq, (count + 1, c))
            
            # if we have a letter on hold, we have added a different character, so add it back
            if hold != None:
                heapq.heappush(pq, hold)
                hold = None
        
        return "".join(res)
            

            