class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)

        seenNums = []
        for i in range(len(nums)):
            if nums[i] not in seenNums:
                seenNums.append(nums[i])
            else:
                nums[i] = ''
        currStreak = 0
        longestStreak = 0
        lastNum = 0
        print(nums)
        for i in range(len(nums)):
            if i == 0:
                lastNum = nums[i]
                curStreak = 1
                longestStreak = 1
            else:
                if nums[i] != '':
                    if nums[i] == lastNum + 1:
                        curStreak += 1
                        if curStreak > longestStreak:
                            longestStreak = curStreak
                    else:
                        curStreak = 1
                    lastNum = nums[i]
        return longestStreak
            