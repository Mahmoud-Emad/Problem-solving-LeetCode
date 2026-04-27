class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        result = []

        if len(nums) <= 1 or len(nums) == k:
            return nums

        for i in nums:
            if map.get(i) != None:
                map[i] += 1
                continue
            map[i] = 0

        for key, value in map.items():
            if value >= 1:
                result.append(key)

        return result[:k]
        