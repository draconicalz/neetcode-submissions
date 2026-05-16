class Solution:
    def canJump(self, nums: List[int]) -> bool:
        counter = 0

        for i in range(len(nums)):
            if counter < nums[i]:
                counter = nums[i]

            counter -= 1

            if i == len(nums) - 1:
                return True
            if counter == -1:
                return False
            