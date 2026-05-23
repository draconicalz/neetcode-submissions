class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        minheap = []
        for key in count:
            heapq.heappush(minheap, [count[key], -key])


        res = []
        while minheap:
            cnt, num = heapq.heappop(minheap)
            for _ in range(cnt):
                res.append(-num)
        return res