class Solution:
    def minChanges(self, s: str) -> int:
        res = 0
        i = 0
        while i < len(s):
            if s[i] != s[i+1]:
                res += 1
            i += 2
        return res
