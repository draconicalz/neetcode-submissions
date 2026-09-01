class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # Get jobs from lowest to highest capital required
        combined = []
        for i in range(len(profits)):
            combined.append((capital[i], profits[i]))
        combined.sort()
        
        curProj = 0
        maxQ = []
        while k > 0:
    
            # Take all jobs that we have the captial for
            # Sort by highest profit in MAX heap
            while curProj < len(combined) and combined[curProj][0] <= w:
                heapq.heappush(maxQ, -combined[curProj][1])
                curProj += 1

            # Do the job that gives us the highest profit, and add profit to w, then decrement 
            if not maxQ: return w
            w += abs(heapq.heappop(maxQ))
            k -= 1
        
        return w
        

