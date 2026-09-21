class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        
        pivot = 0
        
        last = None
        while pivot < len(nums) - 1:
            if abs(nums[pivot]) < abs(nums[pivot + 1]): break
            pivot += 1
        res.append(nums[pivot] ** 2)
        l, r = pivot - 1, pivot + 1
        while l >= 0 and r < len(nums):
            if abs(nums[l]) <= abs(nums[r]):
                res.append(nums[l] ** 2)
                l -= 1
            else:
                res.append(nums[r] ** 2)
                r += 1
        while l >= 0:
            res.append(nums[l] ** 2)
            l -= 1
        while r < len(nums):
            res.append(nums[r] ** 2)
            r += 1
        return res