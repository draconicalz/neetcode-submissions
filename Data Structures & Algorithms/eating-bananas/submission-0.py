class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minRate = 1
        maxRate = max(piles)

        lowestRate = None
        while minRate <= maxRate:
            midRate = (minRate + maxRate) // 2

            hoursLeft = h
            success = True
            for pile in piles:
                if hoursLeft <= 0 or midRate == 0:
                    success = False
                    break
                hoursLeft -= math.ceil(pile / midRate)
                if hoursLeft < 0:
                    success = False
                    break

            if success:
                if not lowestRate:
                    lowestRate = midRate
                else:
                    lowestRate = min(lowestRate, midRate)
                print(lowestRate)
                maxRate = midRate - 1
            else:
                minRate = midRate + 1
            
        return lowestRate

