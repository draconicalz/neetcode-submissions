class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        found = set()
        for num in nums:
            if num not in found:
                found.add(num)
            else:
                return True
        return False