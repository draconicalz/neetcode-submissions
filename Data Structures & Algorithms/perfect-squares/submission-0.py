class Solution:
    def numSquares(self, n: int) -> int:
        nums = []
        for num in range(n):
            sq = num * num
            if sq == n: return 1
            if sq < n:
                nums.append(sq)
            else: break
        
        dp = [n] * (n + 1)
        dp[0] = 0
        for a in range(1, n+1):
            for num in nums:
                if num > a: continue
                if num == a:
                    dp[a] = 1
                    continue
                dp[a] = min(dp[a], dp[a - num] + 1)
        return dp[n]