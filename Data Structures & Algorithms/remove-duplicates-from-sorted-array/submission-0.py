class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num not in seen:
                nums[len(seen)] = num
                seen.add(num)
        return len(seen)