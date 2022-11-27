class Solution:
    def reverse(self, x: int) -> int:
        converted_to_str = str(x)

        if converted_to_str.startswith('-'):
            converted_to_str = converted_to_str.replace("-","")
            if not int(converted_to_str[::-1]) in range(pow(-2, 31), pow(2, 31)-1):
                return 0
            return f"-{int(converted_to_str[::-1])}"
        if not int(converted_to_str[::-1]) in range(pow(-2, 31), pow(2, 31)-1):
            return 0

        return int(converted_to_str[::-1])
