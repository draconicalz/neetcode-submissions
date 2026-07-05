class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]
        for s in strs:
            if not s: return ""
            for i in range(min(len(res), len(s))):
                if s[i] != res[i]: 
                    res = res[:i]
                    break
                if i == len(s) - 1:
                    res = res[:i+1]
        return res