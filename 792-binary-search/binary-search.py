class Solution:
    def search(self, nums: List[int], target: int) -> int:

        size = len(nums)
        min_ = 0
        max_ = len(nums)
        prev = -1
        while True:
            curr = n = (min_ + max_)//2

            if curr == prev:
                return -1
            
            a = nums[n]
            if a == target:
                return n
            else:
                if a > target:
                    max_ = n
                else:
                    min_ = n
                
                prev = n



        