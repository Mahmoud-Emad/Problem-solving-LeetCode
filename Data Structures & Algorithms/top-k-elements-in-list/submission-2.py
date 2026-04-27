class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        result = []

        for i in nums:
            if map.get(i) != None:
                map[i] += 1
                continue
            map[i] = 1

        for key, value in map.items():
            result.append(key)

        result = sorted(result, reverse=True)
        return result[:k]