class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = 0
        for c in s:
            if c == "1": ones += 1
        
        res = ""
        for i in range(len(s) - 1):
            if ones > 1:
                res += "1"
                ones -= 1
            else: res += "0"
        
        if ones == 1: return res + "1"
        else: return res + "0"
