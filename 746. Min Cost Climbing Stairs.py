class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost:
            return 0
        dp0 = cost[0]
        rec = 0
        
        if len(cost)>= 2:
            dp1 = cost[1]
            
        for i in range(2, len(cost)):
            rec = cost[i] + min(dp0, dp1)
            dp0 = dp1
            dp1 = rec
        return min(dp0, dp1)
