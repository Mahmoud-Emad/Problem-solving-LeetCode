class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for c in range(len(nums)):
            for x in range(c + 1, len(nums)):
                if nums[x] == target - nums[c]:
                    return [c, x]