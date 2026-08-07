class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        last = None
        for price in prices:
            if last != None and last < price:
                res += (price - last)
            last = price
        return res