class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        prev, curr = 0, 0 
        for n in nums[0: -1]:
            prev, curr = curr, max(curr, prev+n)
        curr1 = curr
        prev, curr = 0, 0 
        for n in nums[1:]:
            prev, curr = curr, max(curr, prev+n)
        curr2 = curr

        return max(curr1, curr2)


        