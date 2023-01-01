class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left, right = 0, sum(nums)
        for index, element in enumerate(nums):
            print(index, element)
            right -= element
            if left == right:
                return index
            left += element
        return -1
