class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        i = 0
        # do division and multiplication in order first
        while i < len(s):
            if s[i] == " ":
                i += 1
                continue

            # Build the entire number
            if s[i].isdigit():
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1

                if stack and stack[-1] == "*":
                    stack.pop()
                    stack.append(stack.pop() * num)
                elif stack and stack[-1] == "/":
                    stack.pop()
                    stack.append(int(stack.pop() / num))
                else:
                    stack.append(num)

            else:
                stack.append(s[i])
                i += 1
        
        res = stack[0]

        i = 1
        while i < len(stack):
            operator = stack[i]
            num = stack[i + 1]

            if operator == "+":
                res += num
            elif operator == "-":
                res -= num

            i += 2

        return res
