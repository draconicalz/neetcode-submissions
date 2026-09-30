class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        one, two = float("inf"), float("inf")

        for price in prices:
            if price < one:
                two = one
                one = price
            elif price < two:
                two = price
        
        if one == float("inf") or two == float("inf") or (money - one - two) < 0: return money
        return money - one - two