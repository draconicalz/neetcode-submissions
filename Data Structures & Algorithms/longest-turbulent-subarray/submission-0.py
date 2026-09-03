class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        res = 0
        cur = 1
        last = None
        sign = None # True is last sign >, < otherwise
        for num in arr:
            if last == None:
                last = num
                cur = 1
                res = max(cur, res)
                continue
            
            if sign == None:
                if last < num:
                    sign = False
                    cur += 1
                elif last > num:
                    sign = True
                    cur += 1
                else:
                    sign = None
                    cur = 1  
            elif sign == True:
                if last < num:
                    sign = not sign
                    cur += 1
                elif last > num:
                    cur = 2
                else:
                    cur = 1
                    sign = None
            elif sign == False:
                if last > num:
                    sign = not sign
                    cur += 1
                elif last < num:
                    cur = 2
                else:
                    cur = 1
                    sign = None
            last = num
            res = max(res, cur)
             
        
        return res