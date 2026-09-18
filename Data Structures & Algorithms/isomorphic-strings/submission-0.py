class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ST, TS = {}, {}

        for i in range(len(s)):
            c1, c2 = s[i], t[i]
            if (c1 in ST and ST[c1] != c2) or (c2 in TS and TS[c2] != c1): return False
            ST[c1] = c2
            TS[c2] = c1
        return True
        

