class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen = {}
        duplicate = 0
        missing = 0
        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1
        
        for num in seen:
            if seen[num] == 2:
                duplicate = num
        
        for num in range(1, len(nums) + 1):
            if num not in seen:
                missing = num
                break
        return [duplicate, missing]