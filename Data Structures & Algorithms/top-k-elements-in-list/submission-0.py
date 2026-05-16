class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sol = {}
        for num in nums:
            if num not in sol:
                sol[num] = 0
            sol[num] = sol[num] + 1
        
        sortedsol = dict(sorted(sol.items(), key = lambda item: item[1], reverse = True))

        output = []
        for key in sortedsol:
            output.append(key)
            if len(output) >= k: 
                return output
        
        return output
        