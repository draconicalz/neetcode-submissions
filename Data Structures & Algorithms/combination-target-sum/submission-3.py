class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sub = []

        def backtrack(i):
            if i == len(nums):
                return
            
            total = sum(sub)
            if total == target:
                if sub in res: return
                res.append(sub.copy())
                return
            elif total >= target: return
            
            sub.append(nums[i])
            backtrack(i)

            sub.pop()

            backtrack(i + 1)
        backtrack(0)
        return res
            