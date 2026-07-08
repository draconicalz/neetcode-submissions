class Solution:
    def calPoints(self, operations: List[str]) -> int:
        q = []
        for o in operations:
            if o == "+":
                q.append(q[-2] + q[-1])
            elif o == "C":
                q.pop()
            elif o == "D":
                q.append(q[-1] * 2)
            else:
                q.append(int(o))
        return sum(q)