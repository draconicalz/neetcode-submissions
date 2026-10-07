class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        sub = []

        def bt(i):
            if i == len(nums):
                res.append(sub.copy())
                return
            sub.append(nums[i])
            bt(i + 1)
            sub.pop()
            bt(i + 1)

        bt(0)
        return res