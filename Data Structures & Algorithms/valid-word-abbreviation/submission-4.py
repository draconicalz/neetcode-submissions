class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        j = -1
        curnum = ""
        for i in range(len(abbr)):
            
            if abbr[i] == "0": 
                if curnum:
                    curnum += abbr[i]
                    continue
                else: return False
            if abbr[i].isnumeric():
                curnum += abbr[i]
                continue
            
            if curnum:
                j += int(curnum)
                curnum = ""
            
            
            j += 1
            if j >= len(word): return False
            if word[j] != abbr[i]: return False
            
        
        if curnum:
            j += int(curnum)
        return True if j == len(word) - 1 else False
            
