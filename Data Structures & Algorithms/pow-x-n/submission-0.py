class Solution:
    def myPow(self, x: float, n: int) -> float:
        total = x
        negative = False
        if n == 0: return 1
        if n < 0: 
            negative = True
            posn = 0
            while n <= 0:
                posn += 1
                n += 1
            n = posn
        while n > 1:
            n -= 1
            total = total * x

        return x/total if negative else total