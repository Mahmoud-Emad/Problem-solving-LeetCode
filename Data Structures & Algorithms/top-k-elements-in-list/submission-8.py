class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}

        for i in nums:
            if i in freq_map:
                freq_map[i] += 1
                continue
            freq_map[i] = 1

        output = []
        for i in list(freq_map.values()):
            if i > 1:
                output.append(i)
        return output