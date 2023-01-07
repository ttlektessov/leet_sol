# 704. Binary Search
# Day 7, 1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        high, low = len(nums)-1, 0
        while low <= high:
            mid = (high+low)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid+1
            else:
                high = mid-1
        return -1

# 278. First Bad Version
# Day 7, 2

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low, high = 0, n
        bad = 0
        while low <= high:
            mid = (low+high)//2
            if isBadVersion(mid) == False:
                low = mid+1
            elif isBadVersion(mid) == True:
                high = mid-1
                bad = mid
        return bad
