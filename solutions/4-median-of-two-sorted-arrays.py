from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = sorted(nums1 + nums2)
        middle = (len(merged)-1)//2
        if len(merged) % 2:
            return merged[middle]
        else:
            return (merged[middle] + merged[middle+1])/2
