class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowel = set(["a", "e", "i", "o", "u"])
        for i in range(len(words)):
            if words[i][0] in vowel and words[i][-1] in vowel:
                if i == 0:
                    words[i] = 1
                    continue
                words[i] = words[i - 1] + 1
            else:
                if i == 0:
                    words[i] = 0
                    continue
                words[i] = words[i - 1]
        res = []
        for i, j in queries:
            if i == 0:
                res.append(words[j])
            else:
                res.append(words[j] - words[i-1])
        return res
        