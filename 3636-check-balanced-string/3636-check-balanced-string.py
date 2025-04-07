class Solution:
    def isBalanced(self, num: str) -> bool:
        even = 0
        odd = 0

        for i in range(len(num)):
            if (i & 1) == 0:
                even += int(num[i])
            else:
                odd += int(num[i])
        return odd == even
        