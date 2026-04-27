class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count_values = {}
        counted = 0
        for str in strs:
            for sub_str in str:
                counted += ord(sub_str)
  
            if counted in count_values:
                count_values[counted].append(str)
            else:
                count_values[counted] = [str]
            counted = 0
        return list(count_values.values())