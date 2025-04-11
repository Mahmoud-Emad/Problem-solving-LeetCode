class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        numbers = ""
        for n in digits:
            numbers += str(n)
        numbers = str(int(numbers) + 1)
        res = []
        for n in numbers:
            res.append(int(n))
        return res