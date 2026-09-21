class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0
        stuff = [-1] * 101
        for num in nums:
            stuff[num] += 1
            res += stuff[num]
        return res