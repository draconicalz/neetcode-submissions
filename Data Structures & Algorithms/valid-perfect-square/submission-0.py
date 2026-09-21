class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 0, num

        while l <= r:
            m = (l + r) // 2
            if m * m == num: return True

            if m * m < num:
                l = m + 1
            if m * m > num:
                r = m - 1
        
        return False