class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        seen = {}
        for num in nums:
            seen[num] = True
        result = []
        for i in range(1, len(nums) + 1):
            if i not in seen:
                result.append(i)
        return result