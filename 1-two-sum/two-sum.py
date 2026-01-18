class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums2 = sorted(nums)

        def get_ab(nums2):
            w = len(nums2)
            for i, a in enumerate(nums2):
                for j in range(i+1, w):
                    b = nums2[j]
                    if a + b == target:
                        return a, b

        

        a, b = get_ab(nums2)
        result = []
        for index, i in enumerate(nums):
            if i in [a, b]:
                result.append(index)

        return result
