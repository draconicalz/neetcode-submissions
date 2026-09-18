class Solution:
    def firstUniqChar(self, s: str) -> int:
        charToIndex = defaultdict(int)
        for i in range(len(s)):
            if s[i] not in charToIndex:
                charToIndex[s[i]] = i
            else:
                charToIndex[s[i]] = float("inf")
        
        res = float("inf")
        for key, value in charToIndex.items():
            if value < res:
                res = value
        return res if res != float("inf") else -1
                
