class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervalsSorted = sorted(intervals)
        res = []
        curInterval = None
        for interval in intervalsSorted:
            if curInterval == None:
                curInterval = interval
            else:
                if interval[0] > curInterval[1]:
                    res.append(curInterval)
                    curInterval = interval
                elif interval[0] <= curInterval[1]:
                    curInterval = [min(curInterval[0], interval[0]), 
                                    max(curInterval[1], interval[1])]
        res.append(curInterval)
        return res

