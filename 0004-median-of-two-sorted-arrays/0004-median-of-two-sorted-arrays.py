class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_arr = sorted(nums1 + nums2)

        if len(merged_arr) == 0:
            return float(0)

        index   :int = int(len(merged_arr) / 2)
        if len(merged_arr) % 2 == 0:
            before  :int = merged_arr[index - 1]
            after   :int = merged_arr[index]
            return (float(before) + float(after)) / 2 
        else:
            return float(merged_arr[index])
