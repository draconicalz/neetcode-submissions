class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        
        longest = 0

        for n in nums:
            if n - 1 not in nums:
                length = 1
                while True:
                    if n + length in numSet:
                        length += 1
                    else:
                        if length > longest:
                            longest = length
                        break
        return longest


        
            