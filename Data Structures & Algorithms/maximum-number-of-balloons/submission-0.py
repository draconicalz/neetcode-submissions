class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d = {}
        letters = set(['b', 'a', 'l', 'o', 'n'])
        res = 0
        for c in text:
            if c in letters:
                if c not in d:
                    d[c] = 0
                d[c] += 1
        
        while True:
            for key in letters:
                if key not in d: return res
                if key == 'l' or key == 'o':
                    if d[key] < 2: return res
                    d[key] -= 2
                else:
                    if d[key] < 1: return res
                    d[key] -= 1
            res += 1

        return res