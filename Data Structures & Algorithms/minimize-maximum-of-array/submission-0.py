class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        res = nums[0]
        cursum = nums[0]
        for i in range(1, len(nums)):
            cursum += nums[i]
            res = max(res, math.ceil(cursum / (i+1)))
        return res
