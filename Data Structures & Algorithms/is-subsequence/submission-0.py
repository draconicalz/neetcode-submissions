class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: return True
        sIndex = 0
        for i in range(len(t)):
            if t[i] == s[sIndex]:
                sIndex += 1
            
            if sIndex == len(s): return True
        return False