class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        dom = None
        cnt = 0
        for num in nums:
            if not dom:
                dom = num
                cnt += 1
                continue
            
            if num != dom:
                cnt -= 1
                if cnt == 0:
                    dom = None
            if num == dom:
                cnt += 1
        total = 0
        for num in nums:
            if num == dom:
                total += 1

        left, right = 0, total
        for i in range(len(nums)):
            lenLeft, lenRight = i + 1, len(nums) - (i + 1)
            if nums[i] == dom:
                left += 1
                right -= 1
            if left > lenLeft // 2 and right > lenRight // 2:
                return i
        return -1
