class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for str in strs:
            out += str
            out += " "

        return out

    def decode(self, s: str) -> List[str]:
        out = ""
        result = []

        for i in s:
            if i != " ":
                out += i
            else:
                result.append(out)
                out = ""

        return result