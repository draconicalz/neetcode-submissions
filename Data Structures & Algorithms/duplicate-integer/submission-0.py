class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
       found = set()
       for num in nums:
        if num in found:
            return True
        if num not in found:
            found.add(num)
       return False
         