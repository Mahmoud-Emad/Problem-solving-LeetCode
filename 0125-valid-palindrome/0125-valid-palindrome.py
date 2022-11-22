import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.findall("[a-z0-9]", s.lower())
        s = ''.join(i for i in s)
        count = -1
        for i in s:
            if i == s[count]:
                count -= 1
                continue
            else:
                return False
        return True