class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[1] = 1
        
        for curN in range(2, n+1):
            
            for split in range(0, (curN//2) + 1):
                half1 = split
                half2 = curN - split
                  
                dp[curN] = max(dp[half1] * dp[half2], dp[half1] * half2, half1 * half2, half1 * dp[half2], dp[curN])
            
        return dp[n]