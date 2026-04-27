class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        first_map = {}
        second_map = {}

        for i in range(len(s)):
            if s[i] not in first_map:
                first_map[s[i]] = 1
            else:
                first_map[s[i]] += 1

            if t[i] not in second_map:
                second_map[t[i]] = 1
            else:
                second_map[t[i]] += 1

        for k,v in first_map.items():
            if not second_map.get(k):
                return False

            if second_map[k] != v:
                return False
        return True

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_res = []
        for str1 in strs:
            result = []
            for str2 in strs:
                if self.isAnagram(str1, str2):
                    result.append(str1)
                    result.append(str2)
            sorted_res = sorted(list(set(result)))
            if sorted_res not in final_res:
                final_res.append(sorted_res)
        return final_res

