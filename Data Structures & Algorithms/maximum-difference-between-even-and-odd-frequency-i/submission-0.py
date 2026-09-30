class Solution:
    def maxDifference(self, s: str) -> int:
        table = defaultdict(int)

        for c in s:
            table[c] += 1

        mostodd = 0
        leasteven = float("inf")
        for key, value in table.items():
            if value % 2:
                mostodd = max(mostodd, value)
            else:
                leasteven = min(leasteven, value)
        
        return mostodd - leasteven