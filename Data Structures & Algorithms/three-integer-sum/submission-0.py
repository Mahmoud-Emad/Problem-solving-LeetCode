class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []

        for num in nums:
            for num2 in nums[nums.index(num) + 1:]:
                for num3 in nums[nums.index(num2) + 1:]:
                    if num + num2 + num3 == 0 and [num, num2, num3] not in result:
                        result.append([num, num2, num3])

        return result
