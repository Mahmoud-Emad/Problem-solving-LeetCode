class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        store = {}
        for i in nums:
            if i in store:
                return True
            store[i] = i
        return False