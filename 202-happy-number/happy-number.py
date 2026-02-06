class Solution:
    def isHappy(self, n: int) -> bool:

        def sumofsquares(n):
            digits = [int(d) for d in str(n)]
            return sum([x*x for x in digits])

        seen = set()
        def happy(n):
            print(n)
            if n in seen:
                return False
            else:
                seen.add(n)
                
            if n ==2:
                return False
            elif n ==1:
                return True
            return happy(sumofsquares(n))

        return happy(n)
        