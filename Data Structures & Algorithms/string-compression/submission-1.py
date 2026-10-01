class Solution:
    def compress(self, chars: List[str]) -> int:
        l, r = 0, 0
        count = 1
        while r < len(chars):
            chars[l] = chars[r]
            while r < len(chars) - 1 and chars[r + 1] == chars[r]:
                count += 1
                r += 1
            
            if count != 1:
                for c in str(count):
                    l += 1
                    chars[l] = c
                count = 1
            l += 1
            r += 1
        
        return l