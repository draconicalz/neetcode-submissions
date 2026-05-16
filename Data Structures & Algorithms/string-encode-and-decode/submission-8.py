class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0: return ""
        return "»".join(strs) + "»"

    def decode(self, s: str) -> List[str]:
        output = []
        if s == "":
            return output
        constString = ""
        for char in s:
            if char == "»":
                output.append(constString)
                constString = ""
            else:
                constString = constString + char
        return output


