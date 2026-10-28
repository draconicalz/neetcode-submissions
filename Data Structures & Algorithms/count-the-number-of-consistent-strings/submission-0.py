class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowedSet = set()
        for c in allowed:
            allowedSet.add(c)
        res = 0
        for word in words:
            good = True
            for c in word:
                if c not in allowedSet:
                    good = False
                    break
            if good: res += 1
        return res