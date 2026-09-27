class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        curTotal = 0
        res = 0
        l, r = 0, k - 1
        for i in range(k-1):
            curTotal += arr[i]

        while r < len(arr):
            curTotal += arr[r]
            if curTotal / k >= threshold:
                res += 1
            curTotal -= arr[l]
            l, r = l + 1, r + 1

        return res