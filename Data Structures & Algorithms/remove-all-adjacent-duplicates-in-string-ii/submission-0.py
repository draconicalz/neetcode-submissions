class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            stack.append(c)
            # If we don't have k elements we cant have k repeats
            if len(stack) < k: continue

            # Check k elements back if we have a streak
            skip = False
            for i in range(len(stack) - 2, len(stack) - k - 1, -1):
                if stack[i] != c:
                    skip = True
                    break
            if skip: continue

            # If we do, pop them all
            for _ in range(k):
                stack.pop()
            
        return "".join(stack)
            