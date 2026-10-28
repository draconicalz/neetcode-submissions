class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(["a", "e", "i", "o", "u"])
        cur, res, l = 0, 0, 0
        for r in range(len(s)):
            if s[r] in vowels:
                cur += 1
            if r - l + 1 > k:
                if s[l] in vowels:
                    cur -= 1
                l += 1
            res = max(cur, res)
        
        return res
