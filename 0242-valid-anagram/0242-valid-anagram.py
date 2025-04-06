class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        scount, tcount = {}, {}
        for i in range(len(s)):
            if s[i] in scount:
                scount[s[i]] += 1
            else:
                scount[s[i]] = 1

            if t[i] in tcount:
                tcount[t[i]] += 1
            else:
                tcount[t[i]] = 1

        # We have to check if both containing the same chars
        for k, v in scount.items():
            if tcount.get(k) and tcount[k] == v:
                continue
            return False
        return True