class Solution:
    def check(self, nums: List[int]) -> bool:
        drops = 0
        for i in range(len(nums)):
            if nums[i-1] > nums[i]:
                drops += 1
                if drops > 1: return False
        return True