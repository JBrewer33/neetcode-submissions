#number of possible unique paths = dp, m x n grid = 2d
#choice at each step right or down
#dp[i][j] should represent the number of unique paths to get to that point answer will be in dp[n-1][m-1]
#dp[i][j] = dp[i-1][j] + dp[i][j-1] except for left and top edges
#bc start 0,0 = 0
#since we can only move right or down dp[0][j] == 1 and dp[i][0] == 1 can initilize everything to one

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * m] * n

        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[n-1][m-1]