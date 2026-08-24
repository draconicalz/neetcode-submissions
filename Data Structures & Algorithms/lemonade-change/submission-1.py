class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        money = [0, 0]

        for bill in bills:
            print(money)
            if bill == 5:
                money[0] += 1
            if bill == 10:
                if money[0] == 0: return False
                money[0] -= 1
                money[1] += 1
            if bill == 20:
                if money[1] == 0:
                    if money[0] < 3: return False
                    money[0] -= 3
                else:
                    if money[0] == 0: return False
                    money[0] -= 1
                    money[1] -= 1
            
        return True