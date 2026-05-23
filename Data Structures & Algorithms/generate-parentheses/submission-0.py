class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(i, pars, opened, openedleft):
            if i >= n * 2:
                res.append(pars)
                return
            
            if opened < n:
                dfs(i + 1, pars + "(", opened + 1, openedleft + 1)
            elif opened >= n:
                while i < n * 2:
                    pars += ")"
                    i += 1
                res.append(pars)
                return
            
            if openedleft > 0:
                dfs(i + 1, pars + ")", opened, openedleft - 1)
        dfs(0, "", 0, 0)
        return res