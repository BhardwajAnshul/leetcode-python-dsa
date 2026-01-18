class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        break_loop = False
        current = asteroids
        while not break_loop:
            break_loop = True
            f = [current[0]]

            for x in current[1:]:

                if x > 0:
                    f.append(x)
                else:
                    if not f:
                        f.append(x)
                    elif abs(x) == f[-1] :
                        f.pop()
                    elif abs(x) > f[-1] and f[-1]> 0:
                        break_loop = False
                        f[-1] = x
                    elif f[-1] < 0:
                        f.append(x)
            current = f
        
        return current




        