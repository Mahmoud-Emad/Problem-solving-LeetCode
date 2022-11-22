class Solution:
    def compress(self, chars: List[str]) -> int:
        index = 0
        count = 0
        chars.append("")
        for c in chars:
            if c == chars[index]:
                count +=1
            else:
                if count > 1:
                    for d in str(count):
                        chars[index+1] = d
                        index +=1
                if c != "":
                    index +=1
                    chars[index] = c
                    count = 1
        return index+1