class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float('-inf')
        cur = 0
        for i in range(len(nums)):
            if cur < 0:
                cur = 0
            cur += nums[i]

            res = max(cur, res)
        return res
