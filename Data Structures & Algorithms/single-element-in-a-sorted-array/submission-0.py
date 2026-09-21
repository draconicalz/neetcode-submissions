class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if ((m == 0 and nums[m + 1] > nums[m]) or (m == len(nums) - 1 and nums[m - 1] < nums[m]) or
                nums[m - 1] < nums[m] < nums[m + 1]):
                    return nums[m]

            leftSize = m - 1 if nums[m - 1] == nums[m] else m
            if leftSize % 2:
                r = m - 1
            else:
                l = m + 1