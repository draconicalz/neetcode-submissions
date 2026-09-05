class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        if not t: return True
        tIndex = 0
        for i in range(len(s)):
            if s[i] == t[tIndex]:
                tIndex += 1
            if tIndex == len(t): break
            
        return len(t) - tIndex