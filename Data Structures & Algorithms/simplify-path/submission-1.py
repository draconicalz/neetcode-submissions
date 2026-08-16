class Solution:
    def simplifyPath(self, path: str) -> str:
        res = ""
        stack = []
        curword = ""
        for c in path:
            if (c != '.' or (curword != "" and curword != ".")) and c != "/":
                curword += c
            elif c == "/":
                if curword != "." and curword != ".." and curword:
                    stack.append(curword)
                elif curword == ".." and stack:
                    stack.pop()
                curword = ""
            elif c == ".":
                curword += "."
        if curword != "." and curword != ".." and curword:
            stack.append(curword)
        elif curword == ".." and stack:
            stack.pop()
        
        for directory in stack:
            res += "/"
            res += directory

        return res if res else "/"