class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for middle in nums:
            if middle != 0:
                nums[i] = middle
                i+=1
        for y in range(i,len(nums)):
            nums[y] = 0
        return nums
