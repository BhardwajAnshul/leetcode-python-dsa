class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        numbers = set()

        for n in nums:
            if n not in numbers:
                numbers.add(n)
            else:
                numbers.remove(n)

        return list(numbers)[0]
        