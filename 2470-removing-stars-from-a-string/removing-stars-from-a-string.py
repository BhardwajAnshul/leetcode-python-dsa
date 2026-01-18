# class Solution:
#     def removeStars(self, s: str) -> str:

#         f = ''
#         residue = 0
#         for x in s[::-1]:

#             if x!='*':
#                 if residue == 0:
#                     f = f+x
#                 else:
#                     residue-=1

#             else:
#                 residue +=1

#         return f[::-1]
            

            

        
class Solution:
    def removeStars(self, s: str) -> str:

        f = []

        for x in s:

            if x == '*':
                f.pop()
            else:
                f.append(x)

        return ''.join(f)

        return f
            

            

        