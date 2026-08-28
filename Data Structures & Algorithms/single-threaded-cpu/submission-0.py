class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, t in enumerate(tasks):
           t.append(i)         
        tasks.sort(key = lambda t: t[0])
        pq = []
        res = []
        t = tasks[0][0]
        i = 0
        while i < len(tasks) or pq:
            if not pq:
                t = max(t, tasks[i][0])
            while i < len(tasks) and tasks[i][0] <= t:
                heapq.heappush(pq, [tasks[i][1], tasks[i][2]])
                i += 1
            
            time, index = heapq.heappop(pq)
            t += time
            res.append(index)
        
        return res