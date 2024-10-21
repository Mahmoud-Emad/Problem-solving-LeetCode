class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_str = "".join(char.lower() for char in s if char.isalnum())
        return filtered_str == filtered_str[::-1]
