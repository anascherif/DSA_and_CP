class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dic={}
        i=0
        total=0
        def dfs(i):
            if i >=len(cost):return 0
            if i in dic: return dic[i]
            else: 
                total=cost[i]+min(dfs(i+1),dfs(i+2))
                dic[i]=total
                return total
        return min(dfs(0),dfs(1))