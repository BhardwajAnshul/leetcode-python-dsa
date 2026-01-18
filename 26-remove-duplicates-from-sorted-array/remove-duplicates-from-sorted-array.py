class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        start_index  = 0
        start_value = None
        for (index, value) in enumerate(nums):
            if value != start_value:
                nums[start_index] = value
                start_value = value
                start_index+=1

        return start_index


        