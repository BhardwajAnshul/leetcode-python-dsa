class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        maps = {
            "0":0,
            "1":1,
            "2":2,
            "3":3,
            "4":4,
            "5":5,
            "6":6,
            "7":7,
            "8":8,
            "9":9,
        }
        l1 = []
        coff = 1
        for x in num1[::-1]:
            l1.append(coff*maps[x])
            coff = 10*coff
        l1 = l1[::-1]

        mul = 0
        coff = 1
        for n in num2[::-1]:
            n = maps[n]
            mul += coff*sum(l1*n)
            coff = 10*coff

        return str(mul)
