class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        for i in range(0, len(numbers)):
            l = i
            r = len(numbers) - 1
            while r != l:
                if numbers[l] + numbers[r] == target:
                    return [l+1, r+1]
                r -= 1
        