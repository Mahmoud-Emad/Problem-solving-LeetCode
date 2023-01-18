class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == None or len(strs) == 0: return ""
        return self.find_long_common(strs, right=0, left=len(strs) -1)
    
    def find_long_common(self, strs: List[str], right: int, left: int):
        if left == right:
            return strs[left]
        else:
            mid = int((left + right) /2)
            lcp_left = self.find_long_common(strs, left, mid)
            lcp_right = self.find_long_common(strs, mid + 1, right)
            return self.common_prefix(lcp_left, lcp_right)
        
    def common_prefix(self, left: str, right: str):
        min_ = min(len(left), len(right))
        for i in range(0, min_):
            if left[i] != right[i]:
                return left[0:i]
        return left[0:min_]