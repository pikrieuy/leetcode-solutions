class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = []
        for char in s:
            if char.isalnum():
                clean.append(char.lower())

        clean_s = "".join(clean)
        return clean_s == clean_s[::-1]
