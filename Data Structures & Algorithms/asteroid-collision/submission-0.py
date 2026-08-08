class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        res = []
        for i in range(len(asteroids)):
            if not stack and asteroids[i] < 0:
                res.append(asteroids[i])
            elif stack and asteroids[i] < 0:
                while abs(asteroids[i]) >= stack[-1]:
                    if abs(asteroids[i]) == stack[-1]:
                        stack.pop()
                        break
                    stack.pop()
                    if not stack:
                        res.append(asteroids[i])
                        break
            
            if asteroids[i] > 0:
                stack.append(asteroids[i])
        
        res.extend(stack)
        return res
