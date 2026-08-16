class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c != "]":
                stack.append(c)
                continue

            word = ""
            while stack[-1] != "[":
                word += stack.pop()
            stack.pop()  

            word = word[::-1]

            num = ""
            while stack and stack[-1].isnumeric():
                num += stack.pop()

            num = int(num[::-1])

            stack.extend(word * num)

        return "".join(stack)

