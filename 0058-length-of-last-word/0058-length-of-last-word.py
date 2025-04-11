class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = []
        word = ''

        for i in s:
            if i == ' ':
                if len(word) != 0:
                    words.append(word)
                    word = ''
                    continue
            else:
                word += i
                
        # Check last word
        if word:
            words.append(word)
                
        return len(words[-1])