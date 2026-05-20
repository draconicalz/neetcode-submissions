class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0

        seen = set()
        res = 0
        while l <= r and r < len(s):
            if l == r:
                seen.add(s[l])
                r += 1
                res = max(res, len(seen))
            elif r > l:
                if s[r] in seen:
                    seen.remove(s[l])
                    l += 1
                else:
                    seen.add(s[r])
                    res = max(res, len(seen))
                    r += 1
            
        return res