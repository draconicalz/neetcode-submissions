class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        res = float("inf")
        cursum = nums[0]

        l, r = 0, 0
        while l <= r:
            if cursum >= target:
                res = min(res, abs(l - r) + 1)

            if r == len(nums) - 1 or cursum >= target:
                cursum -= nums[l]
                l += 1
            else:
                r += 1
                cursum += nums[r]
        return 0 if res == float("inf") else res
