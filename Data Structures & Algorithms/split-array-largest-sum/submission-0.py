class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # Perform Binary search on result (minimum bucket size)
        l, r = max(nums), sum(nums)

        res = float("inf")

        while l <= r:
            m = (l + r) // 2
            
            remaining = k
            cur = 0
            for i in range(len(nums)):
                total = cur + nums[i]

                # If combined total is too much, split into new bucket
                if total > m:
                    remaining -= 1
                    cur = nums[i]
                    continue
                
                # Otherwise, keep going
                cur = total
            
            # If used k or less buckets, we have a candidate. Go smaller
            if remaining > 0:
                res = min(res, m)
                r = m - 1
            # Otherwise, go bigger
            else:
                l = m + 1
        
        return res





