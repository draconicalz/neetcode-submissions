class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = []
        for char in s:
            letters.append(char)

        for char in t:
            if char not in letters:
                return False
            letters.remove(char)
        
        if len(letters) == 0:
            return True
        return False
        