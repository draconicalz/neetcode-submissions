class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charcounts = defaultdict(int)
        for c in chars:
            charcounts[c] += 1
        res = 0
        for word in words:
            wordcounts = defaultdict(int)
            for c in word:
                wordcounts[c] += 1
            good = True
            for key in wordcounts:
                if key not in charcounts or wordcounts[key] > charcounts[key]:
                    good = False
                    break
            if good: res += len(word)
        return res