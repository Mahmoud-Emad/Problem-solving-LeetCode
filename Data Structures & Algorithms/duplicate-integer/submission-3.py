class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        store = {}
        for i in nums:
            if store.get(i):
                return True
            store[i] = i
        print(store)
        return False