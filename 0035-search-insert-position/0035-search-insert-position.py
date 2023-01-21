class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) -1
        return self.find_number(nums, target, left, right)

    def find_number(self, nums: List[int], target: int, left: int, right: int) -> int:
        mid = int((left + right) / 2)

        while right>=left:

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
            
            nums.append(target)
            nums.sort()
            left = nums.index(target)
            return left