class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixcnt = defaultdict(int)
        prefixcnt[0] = 1
        cur = 0
        res = 0
        for num in nums:
            cur += num
            toGet = cur - k
            res += prefixcnt[toGet]
            prefixcnt[cur] += 1
        return res
