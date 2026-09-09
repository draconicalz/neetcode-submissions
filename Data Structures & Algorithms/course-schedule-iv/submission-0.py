class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        cache = {}
        
        adj = {n: set() for n in range(numCourses)}
        
        for p in prerequisites:
            adj[p[1]].add(p[0])
     
        def dfs(crs):
            if crs not in cache:
                cache[crs] = set()
                for prereq in adj[crs]:
                    cache[crs] |= dfs(prereq)
            cache[crs].add(crs)
            return cache[crs]
        
        
        
        
        for i in range(numCourses):
            dfs(i)
        
        res = []
        for u, v in queries:
            if u in cache[v]:
                res.append(True)
            else:
                res.append(False)
        return res
        