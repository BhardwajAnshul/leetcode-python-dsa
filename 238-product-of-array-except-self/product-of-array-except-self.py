class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num_zeros = 0
        for n in nums:
            if not n:
                num_zeros+=1

        if num_zeros >=2:
            return [0]*len(nums)
        
        non_zero_prod = 1
        for n in nums:
            if n:
                non_zero_prod = n*non_zero_prod

        if num_zeros == 1:
            return [0 if n else non_zero_prod for n in nums]

        else:
            return [non_zero_prod//n for n in nums]
        