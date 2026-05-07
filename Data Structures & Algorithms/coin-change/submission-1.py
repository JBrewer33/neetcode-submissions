#dp not greedy due to varying coin values
#decision at every step, which coin to take
#want to minimize so build array with minimum coins up to that point 1d
#dp[i] = min coints up to point or numb
#dp[i] = f(dp[i-1] + coin)
#bc count > value


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        amountsDp = [float('inf')] * (amount + 1) #store min number of coints to make amount i
        amountsDp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i and amountsDp[i - coin] + 1 < amountsDp[i]:
                    amountsDp[i] = amountsDp[i - coin] + 1
        if amountsDp[amount] != float('inf'):
            return amountsDp[amount]
        return -1