class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nonZero, zero = 0, 0
        while zero < len(nums):
            if nums[zero] != 0:
                nums[nonZero] = nums[zero]
                nonZero += 1
                zero += 1
            else:
                zero += 1
        while nonZero < len(nums):
            nums[nonZero] = 0
            nonZero += 1