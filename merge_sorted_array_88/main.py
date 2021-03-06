from typing import List


class Solution:
    def merge(
        self, nums1: List[int], m: int, nums2: List[int], n: int
    ) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        len1 = m-1
        len2 = n-1
        merged_len = m + n -1
        while len1 >= 0 and len2 >= 0:
            if nums2[len2] > nums1[len1]:
                nums1[merged_len] = nums2[len2]
                len2 -= 1
            else:
                nums1[merged_len] = nums1[len1]
                len1 -= 1

            merged_len -= 1
        nums1[:len2+1] = nums2[:len2+1]
        return nums1
