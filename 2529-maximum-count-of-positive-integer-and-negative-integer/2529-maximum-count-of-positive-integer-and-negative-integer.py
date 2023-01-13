class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        neg = self.num_neg_pos(nums, 0)
        pos = len(nums) - self.num_neg_pos(nums, 1)
        return max(neg, pos)
        
    def num_neg_pos(self, nums: List[int], target: int):
        """Return nums of neg or pos based on the target"""
        left = 0
        right = len(nums)
        
        while left < right:
            mid = int(left + (right - left) / 2)
            if nums[mid] >= target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
        return left