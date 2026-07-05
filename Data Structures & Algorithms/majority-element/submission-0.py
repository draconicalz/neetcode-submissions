class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj = None
        count = 0
        for num in nums:
            if count == 0:
                count += 1
                maj = num
            elif num == maj: count += 1
            elif num != maj: count -= 1
        
        return maj