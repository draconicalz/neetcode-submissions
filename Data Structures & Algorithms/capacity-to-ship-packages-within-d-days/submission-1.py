class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = float("inf")

        while l <= r:
            mcap = (l + r)//2

            cur = 0
            ships = 1
            for i in range(len(weights)):
                if cur + weights[i] > mcap:
                    cur = 0
                    ships += 1
                cur += weights[i]

            if ships <= days:
                res = min(res, mcap)
                r = mcap - 1
            else:
                l = mcap + 1

        return res