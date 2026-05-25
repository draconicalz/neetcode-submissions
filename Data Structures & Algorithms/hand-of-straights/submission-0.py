class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        cnts = Counter(hand)
        q = []

        for key in cnts:
            heapq.heappush(q, key)


        cur = 0
        last = None
        while q:
            if cur == 0:
                cur = groupSize
                last = None
            if last == None:
                num = q[0]
                last = num
            else:
                num = last + 1
                last = num
            if cnts[num] == 0:
                return False
            cnts[num] -= 1
            if cnts[num] == 0 and q[0] == num:
                heapq.heappop(q)
            elif cnts[num] == 0:
                return False
            
            cur -= 1
        
        if cur > 0:
            return False
        return True
            


        

        