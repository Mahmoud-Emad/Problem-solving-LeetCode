class Solution:
    def isPalindrome(self, s: str) -> bool:
        copy = ""
        result = ""
        
        for i in range(len(s)):
            if s[i] == " " or s[i] == "," or s[i] == "." or s[i] == "?" or s[i] == "!":
                continue
            copy += s[i]

        for i in range(len(s) - 1, -1, -1):
            if s[i] == " " or s[i] == "," or s[i] == "." or s[i] == "?" or s[i] == "!":
                continue
            result += s[i]

        copy = copy.lower()
        result = result.lower()
        return copy == result