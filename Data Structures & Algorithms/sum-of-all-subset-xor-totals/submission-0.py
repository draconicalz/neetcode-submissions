class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        curXOR = 0

        def dfs(i):
            nonlocal res
            nonlocal curXOR
            if i >= len(nums):
                res += curXOR
                return
            
            curXOR = curXOR ^ nums[i]
            dfs(i + 1)

            curXOR = curXOR ^ nums[i]
            dfs(i + 1)        
        dfs(0)
        return res