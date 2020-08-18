class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2

        """
        Approach #1:
        - use a dp array and a helper function
        - pretty intuitive
        """
        dp = [-1 for _ in range(n+1)]
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        return self.climb_stairs(n, dp)

    def climb_stairs(self, n, dp):
        if dp[n] != -1:
            return dp[n]
        else:
            dp[n] = self.climb_stairs(n-1, dp) + self.climb_stairs(n-2, dp)
        return dp[n]

        """
        Approach #2
        Two step variables - very intuitive as well
        """
        # one_step = 1
        # two_step = 2
        # new = 0
        # for each in range(2,n):
        #     new = one_step + two_step
        #     one_step = two_step
        #     two_step = new
        # return new

