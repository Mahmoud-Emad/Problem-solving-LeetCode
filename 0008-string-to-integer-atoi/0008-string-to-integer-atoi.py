class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()  # remove leading whitespace
        if not s:
            return 0

        i = 0
        sign = 1
        if s[i] in ['-', '+']:
            sign = -1 if s[i] == '-' else 1
            i += 1

        number = 0
        while i < len(s) and s[i].isdigit():
            number = number * 10 + int(s[i])
            i += 1

        number *= sign
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if number < INT_MIN:
            return INT_MIN
        if number > INT_MAX:
            return INT_MAX

        return number
