class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        cooki = 0
        res = 0
        for i in range(len(g)):
            while cooki < len(s) and s[cooki] < g[i]:
                cooki += 1
            if cooki == len(s): break
            res += 1
            cooki += 1
        return res