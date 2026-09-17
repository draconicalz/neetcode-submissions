class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()
        for email in emails:
            cur = ""
            skip = False
            after = False
            for c in email:
                if (skip and c != "@") or (c == "." and not after): continue
                
                if c == "+" and not after: 
                    skip = True
                    continue

                if c == "@":
                    skip = False
                    after = True
                
                cur += c
            seen.add(cur)
        return len(seen)
