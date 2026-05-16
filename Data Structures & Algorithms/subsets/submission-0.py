class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sols = []

        curSol = []

        def create_subset(i):
            if i == len(nums):
                sols.append(curSol[:])
                return
            
            curSol.append(nums[i])
            create_subset(i+1)

            curSol.pop()
            create_subset(i+1)
        
        create_subset(0)
        return sols