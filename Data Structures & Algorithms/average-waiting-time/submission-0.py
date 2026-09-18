class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        res = 0
        t = 0
        for start, cookTime in customers:
            if t > start:
                res += t - start
                start = t
            t = start + cookTime
            res += cookTime
        return res / len(customers)