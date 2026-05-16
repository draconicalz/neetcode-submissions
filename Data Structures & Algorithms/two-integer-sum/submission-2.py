class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        found = {}

        i = 0
        for num in nums:
            if num in found:
                return [found[num], i]
            else:
                found[target - num] = i
            i += 1