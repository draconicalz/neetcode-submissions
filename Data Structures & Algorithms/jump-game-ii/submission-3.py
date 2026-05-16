class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0

        res = 0
        maximumNum = -1
        reach = 0
        for i in range(0, len(nums)-1):
            if nums[i] - reach > maximumNum:
                maximumNum = nums[i] - reach
            
            if reach == 0:
                res += 1
                reach = maximumNum
                maximumNum = -1
            
            if i + reach >= len(nums) - 1:
                break
            
            reach -= 1

        
        return res