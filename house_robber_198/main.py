from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        naive approach:
        Maintain a even and odd variable
        for every even index compare with:
            max(existing_even + current VS existing_odd)
        do the same for odd and get the result
        ************************************************
        Better way:
        Take a DP array of length of the array
        assign dp[0] to first value 
        dp[1] if array is longer to max(num[0],num[1])
        If any longer, run a loop and do this:
            dp[i] = max(dp[i-1], dp[i-2]+ current_num)
        """
        # NAIVE
        """
        even = 0
        odd = 0
        for index, val in enumerate(nums):
            if index % 2 == 0:
                # Even index
                even = max(even + val, odd)
            else:
                # Odd index
                odd = max(odd + val, even)
        return max(odd, even)
        """
        # DP approach
        dp = [-1 for _ in range(len(nums))]
        dp[0] = nums[0]
        if len(nums) > 1:
            dp[1] = max(nums[0], nums[1])
        if len(nums) > 2:
            for i in range(2, len(nums)):
                dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[-1]


sol = Solution()
print(f"Output ->{sol.rob([1, 2, 3, 1])}")
