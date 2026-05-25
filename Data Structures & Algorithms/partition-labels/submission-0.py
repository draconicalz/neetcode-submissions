class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        charToLastIndex = {}

        for i in range(len(s) - 1, -1, -1):
            if s[i] not in charToLastIndex:
                charToLastIndex[s[i]] = i
        
        res = []
        end = float("-inf")
        size = 0
        for i in range(len(s)):
            size += 1
            end = max(charToLastIndex[s[i]], end)

            if i == end:
                res.append(size)
                size = 0
                end = float("-inf")


        return res
