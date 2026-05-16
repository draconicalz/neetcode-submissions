class Solution:
    def isValid(self, s: str) -> bool:
        if not s: return False
        stack = []

        pars = {
            "(" : ")",
            "[" : "]",
            "{" : "}"
        }
        for char in s:
            if char in pars.keys():
                stack.append(char)
            else:
                if not stack: return False
                popped = stack.pop()
                if pars[popped] != char:
                    return False
        
        return not stack

        