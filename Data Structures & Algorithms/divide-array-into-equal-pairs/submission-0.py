class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        counts = defaultdict(int)
        for n in nums:
            counts[n] += 1
        for key, val in counts.items():
            if val % 2: return False
        return True