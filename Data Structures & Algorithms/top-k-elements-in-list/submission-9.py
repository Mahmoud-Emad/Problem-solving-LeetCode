class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}

        for i in nums:
            if i in freq_map:
                freq_map[i] += 1
                continue
            freq_map[i] = 1

        output = []
        for k, v in freq_map.items():
            if v > 1:
                output.append(k)
        return output