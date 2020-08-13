from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        - naive way would be to pop out last element and push to the front 
        - Repeat this 'k' times

        - This logic below is weird, but works and I found this on youtube/LC
        """

        # Doing this because there might be cases where
        # the len(nums) is less than 'k'
        k = k % len(nums)

        nums = self.reverse(nums, 0, len(nums)-1)
        nums = self.reverse(nums, 0, k-1)
        nums = self.reverse(nums, k, len(nums)-1)

        return nums

    def reverse(self, nums, start, end):
        while(start < end):
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
        return nums
