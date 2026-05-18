class Solution:
    def isHappy(self, n: int) -> bool:
        hashmap = {}
        while n != 1:
            newn = 0
            for num in str(n):
                newn += int(num) ** 2
            if hashmap.get(newn): return False
            hashmap[newn] = 1
            n = newn
        return True