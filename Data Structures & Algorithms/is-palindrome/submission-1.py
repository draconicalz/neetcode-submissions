class Solution:
    def isPalindrome(self, s: str) -> bool:
        noSpecial = []
        for char in s:
            if char.isalpha():
                noSpecial.append(char.lower())
            if char.isdigit():
                noSpecial.append(char)

        for i in range(len(noSpecial) // 2):
            if noSpecial[i] != noSpecial[-(i+1)]:
                return False

        return True

        