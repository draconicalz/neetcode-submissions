class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        countTarget = {}
        windowCounts = {}

        for c in t:
            countTarget[c] = 1 + countTarget.get(c, 0)
            windowCounts[c] = 0
        
        res, resLen = [-1, -1], float("inf")
        have, need = 0, len(countTarget)
        l = 0
        for r in range(len(s)):
            c = s[r]
            windowCounts[c] = 1 + windowCounts.get(c, 0)

            if c in countTarget and windowCounts[c] == countTarget[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)
                windowCounts[s[l]] -= 1
                if s[l] in countTarget and windowCounts[s[l]] < countTarget[s[l]]:
                    have -= 1
                l += 1
            
        l, r = res

        return s[l:r+1] if resLen != float("inf") else ""

