class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        pairs = list(zip(y, x))
        pairs.sort(reverse = True)
        
        y = [i[0] for i in pairs]
        x = [i[1] for i in pairs]
        res = 0
        total = 0
        seenx = set()
        for i in range(len(x)):
            if x[i] not in seenx:
                seenx.add(x[i])
                res += y[i]
                total += 1
            if total == 3: break
        return -1 if total < 3 else res