class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rq = deque()
        dq = deque()

        for i in range(len(senate)):
            if senate[i] == "R":
                rq.append(i)
            else:
                dq.append(i)
        
        while rq and dq:
            curR = rq.popleft()
            curD = dq.popleft()

            if curR < curD:
                rq.append(curR + len(senate))
            else:
                dq.append(curD + len(senate))
        
        if not dq: return "Radiant"
        return "Dire"