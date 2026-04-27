class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        left = []
        right = []

        for idx, num in enumerate(nums):
            if len(nums) - 1 == idx:
                if num - 1 == nums[idx - 1]:
                    left.append(num)
                return len(left) if len(left) > len(right) else len(right)

            if num + 1 == nums[idx + 1]:
                left.append(num)
            else:
                right.append(num)
                continue