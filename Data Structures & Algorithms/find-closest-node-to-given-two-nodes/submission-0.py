class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def bfs(start):
            dist = [-1] * len(edges)
            node = start
            depth = 0

            while node != -1 and dist[node] == -1:
                dist[node] = depth
                depth += 1
                node = edges[node]

            return dist

        dist1 = bfs(node1)
        dist2 = bfs(node2)

        res = -1
        best = float("inf")

        for i in range(len(edges)):
            if dist1[i] != -1 and dist2[i] != -1:
                worst = max(dist1[i], dist2[i])

                if worst < best:
                    best = worst
                    res = i

        return res
