class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        res = []
        for word in words:
            saved_word = ""
            for char in word:
                if len(char) == 0:
                    continue

                if char == separator:
                    if len(saved_word) > 0:
                        res.append(saved_word)
                    saved_word = ""
                    continue

                saved_word += char
            if len(saved_word) > 0:
                res.append(saved_word)

        return res
            