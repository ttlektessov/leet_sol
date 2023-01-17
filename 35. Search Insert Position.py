class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                high = mid - 1
            elif target > nums[mid]:
                low = mid + 1
                
        if nums[mid]>target:
                return mid
                
        return mid+1
