class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0: return 0
        def isValid(thresh):
            i, cnt = 0, 0
            while i < len(nums) - 1:
                diff = abs(nums[i] - nums[i + 1])
                if diff <= thresh:
                    cnt += 1
                    i += 2
                else:
                    i += 1
                if cnt == p: return True
            return False
        l, r = 0, 10 ** 9 # bullshit
        nums.sort()
        res = 10**9
        while l <= r:
            m = l + (r - l) // 2
            
            if isValid(m):
                res = m
                r = m - 1
            else:
                l = m + 1
        return res