class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = defaultdict(int)
        
        for c in s:
            counts[c] += 1
        
        # arrange char counts in desc order
        pq = []
        for c, count in counts.items():
            heapq.heappush(pq, (-count, c))
            
        # pop max and decrease by 1 and re add while building our result
        res = ""
        last = None
        while pq:
            count, c = heapq.heappop(pq)
            res += c
            if last != None:
                    heapq.heappush(pq, last)
                    last = None
            if count + 1 < 0:
                last = (count + 1, c)
        
        return res if len(res) == len(s) else ""   