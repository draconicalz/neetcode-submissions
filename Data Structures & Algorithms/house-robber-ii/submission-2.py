class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def robHelp(houses):
            rob1, rob2 = 0, 0

            for n in houses:
                temp = max(rob1 + n, rob2)
                rob1 = rob2
                rob2 = temp
            
            return rob2
        
        if len(nums) > 1: return max(robHelp(nums[1:]), robHelp(nums[:-1]))
        else: return robHelp(nums)