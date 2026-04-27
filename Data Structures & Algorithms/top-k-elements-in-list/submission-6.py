class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}

        for i in nums:
            if i in freq_map:
                freq_map[i] += 1
                continue
            freq_map[i] = 1

        sorted_elements = sorted(freq_map,  reverse=True)
        return sorted_elements[:k]