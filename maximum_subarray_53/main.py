from typing import List


class Solution:
    """
    Easy approach!
    - Iter through the list
    - If the item before you is greater than 0, ie, positive
        - Add it with the current element you are at
    - return the max of all these elements!
    """
    """
    DP approach ish
    maintain a DP variable -> init to 0
    dp = max(dp + each_num, each_num)
    if this value is larger than existing max
        - Update max val
    """
    def maxSubArray(self, nums: List[int]) -> int:
        # APPROACH #1
        # for ind in range(1, len(nums)):
        #     if nums[ind-1] > 0:
        #         nums[ind] += nums[ind-1]
        # return max(nums)
        # APPROACH #2
        dp = 0
        max_val = None
        for each_num in nums:
            dp = max(dp + each_num, each_num)
            if max_val is None or dp > max_val:
                max_val = dp
        return max_val

