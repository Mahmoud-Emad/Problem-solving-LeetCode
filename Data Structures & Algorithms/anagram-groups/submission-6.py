from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count_values = defaultdict(list)
        count = [0] * 26
        for str in strs:
            for sub_str in str:
                count[ord(sub_str) - ord('a')] += 1
            count_values[tuple(count)].append(str)
        return list(count_values.values())