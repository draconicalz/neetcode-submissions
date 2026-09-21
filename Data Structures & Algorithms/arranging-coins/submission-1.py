class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 0, n

        best = n
        while l <= r:
            m = (l + r) // 2
            req = m * (m + 1) // 2

            if req <= n:
                best = m
                l = m + 1
            else:
                r = m - 1

        return best 