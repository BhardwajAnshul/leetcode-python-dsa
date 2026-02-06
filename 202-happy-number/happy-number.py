class Solution:
    def isHappy(self, n: int) -> bool:

        def sumofsquares(n):
            digits = [int(d) for d in str(n)]
            return sum([x*x for x in digits])

        seen = set()
        def happy(n):
            if n ==1:
                return True
            elif n in seen:
                return False
            seen.add(n)
            return happy(sumofsquares(n))

        return happy(n)
        