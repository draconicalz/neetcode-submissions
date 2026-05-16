class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        for num in nums:
            j = 0
            for num2 in nums:
                if i != j:
                    if num + num2 == target:
                        return [i, j]
                j = j + 1
            i = i + 1
        return -1
        