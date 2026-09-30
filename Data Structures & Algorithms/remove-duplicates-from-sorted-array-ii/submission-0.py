class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = defaultdict(int)
        curIndex = 0
        k = 0
        for num in nums:
            if seen[num] < 2:
                seen[num] += 1
                nums[curIndex] = num
                curIndex += 1
        return curIndex