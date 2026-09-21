class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = defaultdict(int)
        for c in magazine:
            mag[c] += 1
        for c in ransomNote:
            if mag[c] == 0: return False
            mag[c] -= 1
        return True