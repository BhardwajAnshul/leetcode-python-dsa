class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        h = h-len(piles)

        def isValid(i):
            total_hours = 0
            for p in piles:
                hours = (p-1)//i
                # if not p%i:
                    # hours = hours-1
                total_hours+= hours
            return total_hours - h

        # if negative eat less, if positive eat less

        left, right = 1, max(piles)
        while left <= right:
            curr = (left+right)//2
            if isValid(curr) <= 0:
                right = curr-1
            else:
                left = curr+1
        if isValid(curr) > 0:
            return curr+1
        else:
            return curr




        