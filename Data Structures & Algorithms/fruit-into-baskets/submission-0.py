class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        counts = defaultdict(int)
        types = 0
        cur = 0
        res = 0
        for r in range(len(fruits)):
            if counts[fruits[r]] == 0:
                types += 1
            counts[fruits[r]] += 1
            cur += 1
            
            while types > 2:
                counts[fruits[l]] -= 1
                cur -= 1
                if counts[fruits[l]] == 0:
                    types -= 1
                l += 1
            
            res = max(res, cur)
        return res