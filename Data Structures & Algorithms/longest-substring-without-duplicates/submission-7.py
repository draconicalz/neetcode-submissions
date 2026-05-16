class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l = 0
        r = 0
        res = 1
        curLen = 1
        curLetters = set()
        curLetters.add(s[0])
        while r < len(s) - 1:
            r += 1
            curLen += 1
            if s[r] in curLetters:
                while s[r] in curLetters:
                    curLetters.remove(s[l])
                    curLen -= 1
                    l += 1
            curLetters.add(s[r])

            res = max(res, curLen)
        
        return res
            


        