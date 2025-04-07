class Solution:
    def isBalanced(self, num: str) -> bool:
        even_numbers = []
        odd_numbers = []

        for i in range(len(num)):
            if i % 2 == 0:
                odd_numbers.append(int(num[i]))
            else:
                even_numbers.append(int(num[i]))

        is_balanced = sum(even_numbers) == sum(odd_numbers)
        return is_balanced