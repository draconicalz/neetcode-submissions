class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        def dfs(i, parts):
            if len(parts) == 4:
                if i == len(s):
                    res.append(".".join(parts))
                return
            for length in range(1, 4):
                if i + length > len(s):
                    break
                chunk = s[i: i + length]
                
                if (len(chunk) > 1 and chunk[0] == "0") or int(chunk) > 255:
                    break
                
                dfs(i + length, parts + [chunk])
        
        dfs(0, [])
        return res