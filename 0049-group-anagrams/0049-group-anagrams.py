class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count_values = {}
        for str in strs:
            count = [0] * 26
            for sub_str in str:
                count[ord(sub_str) - ord('a')] += 1

            if tuple(count) not in count_values:
                count_values[tuple(count)] = []
            count_values[tuple(count)].append(str)
        return list(count_values.values())
