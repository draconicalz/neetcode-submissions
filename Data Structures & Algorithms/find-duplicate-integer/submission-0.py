class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        foundNums = []
        for num in nums:
            if num not in foundNums:
                foundNums.append(num)
            else:
                return num
        
        return -1