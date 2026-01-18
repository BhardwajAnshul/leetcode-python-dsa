# class Solution:
#     def minCostClimbingStairs(self, cost: List[int]) -> int:


#         @lru_cache(None)
#         def total_cost(i):

#             if i-2 < 0:
#                 return 0
#             else:
#                 return min(
#                 total_cost(i-1)+cost[i-1],
#                 total_cost(i-2) + cost[i-2]
#                 )

#         total_len = len(cost)

#         return total_cost(total_len)


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev2 = prev1 = 0

        for i in range(2, len(cost) + 1):
            curr = min(
                prev1 + cost[i - 1],
                prev2 + cost[i - 2]
            )
            prev2, prev1 = prev1, curr

        return prev1
