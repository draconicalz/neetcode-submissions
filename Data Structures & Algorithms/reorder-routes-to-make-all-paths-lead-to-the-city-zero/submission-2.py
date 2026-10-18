class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph=[[] for _ in range(n)]
        for u,v in connections:graph[u].append((v,1));graph[v].append((u,0))
        answer=0;stack=[(0,-1)]
        while stack:
            node,parent=stack.pop()
            for neighbor,cost in graph[node]:
                if neighbor!=parent:answer+=cost;stack.append((neighbor,node))
        return answer

