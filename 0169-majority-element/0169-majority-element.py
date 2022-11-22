class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict_ = {}
        for num in nums:
            dict_[num] = 0
        
        for num in nums:
            for k,v in dict_.items():
                if num == k:
                    dict_[k] += 1
        max_ = max(dict_.values())
        for k,v in dict_.items():
            if v == max_:
                return k