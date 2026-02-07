class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        if len(nums)==1:
            return nums[0]
        
        start = nums[0]
        for num in nums[1:]:
            start = start ^ num
        return start
        