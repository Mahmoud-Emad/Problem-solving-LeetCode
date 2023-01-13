class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        
        while left < right:
            mid = int(left + (right - left) / 2)
            if nums[mid] >= target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1

        return left if len(nums) > left and nums[left] == target else -1