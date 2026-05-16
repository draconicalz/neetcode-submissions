class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        subset = []
        def dfs(i):
            if i >= len(nums):
                return
            
            total = sum(subset)
            if total == target:
                if subset in res:
                    return
                res.append(subset.copy())
                return
            elif total >= target:
                return

            subset.append(nums[i])
            dfs(i)

            dfs(i+1)

            subset.pop()
            dfs(i+1)
        
        dfs(0)
        return res