class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount+1)
        dp[0] = 0

        for coin in coins:
            for curr_coin in range(coin, amount+1):
                dp[curr_coin] = min(dp[curr_coin], dp[curr_coin - coin] + 1)
        
        return dp[amount] if dp[amount]!= float('inf') else -1
