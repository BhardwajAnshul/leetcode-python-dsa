class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        size = len(digits)

        digits[-1] = digits[-1] + 1
        append_leading_one = False
        for i in range(size-1, -1, -1):
            if digits[i] > 9:
                digits[i] = digits[i]%10
                if i-1>=0:
                    digits[i-1] = digits[i-1] + 1 
                else:
                    append_leading_one = True

        if append_leading_one:
            digits = [1] + digits

        return digits


        