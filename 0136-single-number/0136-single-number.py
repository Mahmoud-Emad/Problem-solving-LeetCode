class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        items = {}
        for n in nums:
            if n in items:
                items[n] += 1
            else:
                items[n] = 1

        for k, v in items.items():
            if v == 1:
                return k
