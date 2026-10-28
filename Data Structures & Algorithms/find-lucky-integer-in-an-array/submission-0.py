class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counts = defaultdict(int)
        for num in arr:
            counts[num] += 1
        
        res = -1
        for key in counts:
            if counts[key] == key:
                res = max(key, res)
        return res