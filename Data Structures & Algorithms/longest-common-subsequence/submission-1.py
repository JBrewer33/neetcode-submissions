#only need to return length so likely space opt possible
#choice at each step, take letter or not, can only take if letter in 1 is also in 2
#need to do bottom up to "build" substrings
#dp[i][j] == 1 + dp[i+1][j+1] if we're adding else == max of i+1 or j+1
#return dp[0][0]

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for i in range(len(text2) + 1)] for j in range(len(text1) + 1)]

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1,  -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        return dp[0][0]
