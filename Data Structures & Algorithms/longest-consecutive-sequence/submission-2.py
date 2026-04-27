class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        left = []
        right = []

        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return 0

        for idx, num in enumerate(nums):
            if len(nums) - 1 == idx:
                if num - 1 == nums[idx - 1]:
                    left.append(num)
                print('l: ', left)
                print('r: ', right)
                return len(left) if len(left) > len(right) else len(right)

            if num + 1 == nums[idx + 1]:
                left.append(num)
            else:
                right.append(num)
                continue
