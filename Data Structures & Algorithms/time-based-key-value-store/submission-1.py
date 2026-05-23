class TimeMap:

    def __init__(self):
        self.hm = {}
        self.timeToIndex = {}
        self.times = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not self.hm.get(key):
            self.hm[key] = []
        self.hm[key].append([value, timestamp])
        
        if not self.timeToIndex.get(key):
            self.timeToIndex[key] = {}
        self.timeToIndex[key][timestamp] = len(self.hm[key]) - 1

        if not self.times.get(key):
            self.times[key] = []
        self.times[key].append(timestamp)


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hm:
            return ""

        searchSpace = self.times[key]

        l, r = 0, len(searchSpace) - 1
        res = ""

        while l <= r:
            m = (l + r) // 2

            if searchSpace[m] <= timestamp:
                res = self.hm[key][self.timeToIndex[key][searchSpace[m]]][0]
                l = m + 1
            else:
                r = m - 1

        return res

        
