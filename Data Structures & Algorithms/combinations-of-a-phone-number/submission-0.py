class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        numToChar = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz",
            0: "+"
        }
        def dfs(i, cur):
            if i == len(digits):
                if cur:
                    res.append(cur)
                return True
            for c in numToChar[int(digits[i])]:
                cur += c
                dfs(i + 1, cur)
                cur = cur[:-1]
        
        dfs(0, "")
        return res