class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counts = defaultdict(int)
        
        for n in arr:
            counts[n] += 1
        
        for n in arr:
            if counts[n] == 1:
                k -= 1
                if k == 0: return n
        return ""