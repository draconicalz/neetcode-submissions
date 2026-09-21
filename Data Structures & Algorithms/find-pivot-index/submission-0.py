class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        curSum = 0
        last = 0
        for i in range(len(nums)):
            curSum += last
            total -= nums[i]
            last = nums[i]
            if curSum == total: return i
        
        return -1