class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = 0
        W = 0

        for r in range(k):
            if blocks[r] == "W":
                W += 1
        r += 1
        res = W

        while r < len(blocks):
            if blocks[l] == "W":
                W -= 1
            if blocks[r] == "W":
                W += 1

            l += 1
            r += 1

            res = min(res, W)

        return res