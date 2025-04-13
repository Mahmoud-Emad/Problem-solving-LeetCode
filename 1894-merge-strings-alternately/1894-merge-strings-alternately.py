class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        max_len = len(word1)
        if len(word2) > max_len:
            max_len = len(word2)

        word = ""
        for i in range(max_len):
            if i < len(word1):
                word += word1[i]
            if i < len(word2):
                word += word2[i]

        return word