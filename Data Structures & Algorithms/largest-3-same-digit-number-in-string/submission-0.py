class Solution:
    def largestGoodInteger(self, num: str) -> str:
        combo = 0
        last = None
        biggest = None
        for d in num:
            if d != last: combo = 1
            else: combo += 1
            last = d
            if combo == 3 and (not biggest or d > biggest):
                biggest = d
        return biggest * 3 if biggest else ""
