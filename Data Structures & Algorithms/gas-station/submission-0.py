class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): return -1

        curTotal = 0
        start = 0
        for i in range(len(gas)):
            curTotal += (gas[i] - cost[i])
            if curTotal < 0: 
                curTotal = 0
                start = i + 1

        return start
        
        

            