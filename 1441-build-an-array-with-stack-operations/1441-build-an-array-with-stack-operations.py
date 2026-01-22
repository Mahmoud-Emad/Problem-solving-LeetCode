class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result = []
        j = 0  # pointer for target

        for i in range(1, target[-1] + 1):
            result.append("Push")

            if i == target[j]:
                j += 1
            else:
                result.append("Pop")

        return result
