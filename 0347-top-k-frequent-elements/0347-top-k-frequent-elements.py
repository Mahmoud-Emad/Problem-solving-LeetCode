class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}

        for i in nums:
            if i in freq_map:
                freq_map[i] += 1
                continue
            freq_map[i] = 1

        # print(freq_map)
        res = []
        for k_, v in freq_map.items():
            res.append([v, k_])

        res.sort(reverse=True)

        res2 = []
        for i in res:
            res2.append(i[1])

        return res2[:k]