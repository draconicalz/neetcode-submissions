class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        if len(nums) == 1: return 0
        while l <= r:
            m = (l + r) // 2

            if ((m == 0 and nums[m] > nums[m + 1]) or (m == len(nums) - 1 and nums[m] > nums[m - 1]) or 
                nums[m] > nums[m - 1] and nums[m] > nums[m + 1]): return m
            
            if (nums[m - 1] <= nums[m] <= nums[m + 1]) or (m == 0 and nums[m] <= nums[m + 1]):
                l = m + 1
            else:
                r = m - 1
