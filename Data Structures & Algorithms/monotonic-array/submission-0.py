class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = None
        last = nums[0]
        for i in range(1, len(nums)):
            if increasing == None:
                if nums[i] < last:
                    increasing = False
                if nums[i] > last:
                    increasing = True
            else:
                if increasing and nums[i] < last: return False
                if not increasing and nums[i] > last: return False
            last = nums[i]
        return True