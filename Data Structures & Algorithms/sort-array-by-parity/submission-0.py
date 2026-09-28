class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] % 2:
                while l <= r and nums[r] % 2:
                    r -= 1
                if l <= r:
                    temp = nums[r]
                    nums[r] = nums[l]
                    nums[l] = temp
                    r -= 1
            l += 1
        return nums