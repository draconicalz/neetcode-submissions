class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        e = defaultdict(int)
        for height in heights:
            e[height] += 1
        
        start = min(heights)
        
        res = 0
        for i in range(len(heights)):
            if heights[i] != start:
                res += 1
            e[start] -= 1
            if e[start] == 0 and start != max(heights):
                start += 1
                while start not in e: start += 1
            
        
        return res