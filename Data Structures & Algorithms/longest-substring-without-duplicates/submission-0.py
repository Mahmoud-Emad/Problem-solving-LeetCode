class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Soluton one i found
        # Initialze an empty string word
        # 1. Loop on the array
        # 2. if the current s not in the word add it to the word
        # 3. if not, store the word to an array
        # 4. Loop on the store arry and return the longest word
        words = []
        word = ""

        for i in range(len(s)):
            char = s[i]
            if char in word:
                words.append(word)
                word = word[i + 1 : ]
            word += char

        words.append(word)

        return max(len(w) for w in words)