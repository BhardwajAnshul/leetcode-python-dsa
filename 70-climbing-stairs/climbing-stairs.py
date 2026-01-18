class Solution:
    def climbStairs(self, n: int) -> int:

        @lru_cache(None)
        def step(n):
            if n == 1:
                return 1
            elif n == 2:
                return 2
            else:
                return step(n-2) + step(n-1)

        return step(n)
        