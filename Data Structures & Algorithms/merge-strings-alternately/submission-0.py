class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        for i in range(min(len(word1), len(word2))):
            res += word1[i]
            res += word2[i]
        
        totali = len(res) // 2
        res += word1[totali:]
        res += word2[totali:]
        return res