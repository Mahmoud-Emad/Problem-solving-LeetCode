class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_map = {}
        t_map = {}
        for i in s:
            if  s_map.get(i):
                v = s_map.get(i)
                s_map[i] = v + 1
                continue
            s_map[i] = 1

        for i in t:
            if  t_map.get(i):
                v = t_map.get(i)
                t_map[i] = v + 1
                continue
            t_map[i] = 1

        for k,v in s_map.items():
            if not t_map.get(k):
                return False

            if t_map[k] != v:
                return False
        return True