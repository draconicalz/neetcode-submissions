class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        adj = {i:[] for i in range(1,n+1)}
        
        for p, t in trust:
            adj[p].append(t)
        
        candidate = None
        for p in adj:
            if len(adj[p]) == 0:
                if candidate: return -1
                candidate = p
        if not candidate: return -1
        
        for p in adj:
            if candidate not in adj[p] and p != candidate: return -1
        
        return candidate