class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1: return int(tokens[0])
        stack = []
        curVal = 0
        for token in tokens:
            if token.isdigit() or len(token) > 1:
                stack.append(int(token))
            else:
                val1 = stack.pop()
                val2 = stack.pop()
                if token == "+":
                    stack.append(val1 + val2)
                elif token == "*":
                    stack.append(val1 * val2)
                elif token == "-":
                    stack.append(val2 - val1)
                elif token == "/":
                    stack.append(int(val2 / val1))

                print(stack)

        return stack[0]
                

        