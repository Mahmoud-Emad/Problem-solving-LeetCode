class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """   

        i = 0
        j = 0

        while i < m+n:
            if nums1[i] == 0:
                if j < n:
                    nums1[i] = nums2[j]
                    j += 1
            i += 1

        for i in range(len(nums1)):
            for j in range(i + 1, len(nums1)):
                if nums1[j] < nums1[i]:
                    iel = nums1[i]
                    nums1[i] = nums1[j]
                    nums1[j] = iel
