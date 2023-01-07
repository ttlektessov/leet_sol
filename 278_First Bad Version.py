class Solution:
    def firstBadVersion(self, n: int) -> int:
        low, high = 0, len(n)-1
        bad = 0
        while low <= high:
            mid = (low+high)//2
            if isBadVersion(mid) == False:
                high
