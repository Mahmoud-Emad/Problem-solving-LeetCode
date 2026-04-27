class Solution:
    def isPalindrome(self, s: str) -> bool:
        copy = ""
        result = ""
        
        for i in range(len(s)):
            if s[i] == " " or s[i] == "," or s[i] == "." or s[i] == "?" or s[i] == "!" or s[i] == "'" or s[i] == "`":
                continue
            copy += s[i]

        print('copy1: ' + copy)
        
        for i in range(len(s) - 1, -1, -1):
            if s[i] == " " or s[i] == "," or s[i] == "." or s[i] == "?" or s[i] == "!" or s[i] == "'" or s[i] == "`":
                continue
            result += s[i]

        copy = copy.lower()
        result = result.lower()
        print('copy: ' + copy)
        print('result: ' + result)
        return copy == result