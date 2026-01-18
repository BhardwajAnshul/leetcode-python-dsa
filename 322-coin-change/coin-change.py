class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        costs = [float('inf')]*(amount+1)

        costs[0] = 0

        for i in range(1,amount+1):
            for coin in coins:
                if i - coin >= 0:
                    costs[i] = min(costs[i], costs[i-coin]+1)

        return costs[amount] if costs[amount]!=float('inf') else -1
        