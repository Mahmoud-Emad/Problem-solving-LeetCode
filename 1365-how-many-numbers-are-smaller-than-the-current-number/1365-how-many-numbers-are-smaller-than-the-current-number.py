class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        max_number = 0
        result = []
        for i in nums:
            for j in nums:
                if i > j:
                    max_number += 1
            result.append(max_number)
            max_number = 0
        return result