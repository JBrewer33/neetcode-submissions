class Solution:
    def climbStairs(self, n: int) -> int:
        #number of distinct way to climb to the top
        #option at every step = climb 1 or climb 2
        #base case 0 steps left 1 step left?
        #at each n either n + 1 or n + 2
        #so at each [i] the number of ways to reach the step is sum of two previous steps [i-1] + [i-2]
        #bc = 2 = 2

        if n < 2:
            if n < 1:
                return 0
            return 1

        dp = [0] * n
        dp[0] = 1
        dp[1] = 2

        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n-1]

