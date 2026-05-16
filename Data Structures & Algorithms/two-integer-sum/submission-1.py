class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenNums = {}
        for i in range(0, len(nums)):
            if target - nums[i] in seenNums:
                return [seenNums[target-nums[i]], i]
            seenNums[nums[i]] = i
        return false
        