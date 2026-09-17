class Solution:
    def isSubsetSum(self, arr: list[int], sum: int) -> bool:
        # code here
        n=len(arr)
        dp=[[-1 for _ in range(sum+1)] for _ in range(n)]
        def fun(i,curr):
            if curr==0:
                return True
            if i==n or curr<0:
                return False
            if dp[i][curr]!=-1:
                return dp[i][curr]
            take=fun(i+1,curr-arr[i])
            nt=fun(i+1,curr)
            dp[i][curr]=take or nt
            return dp[i][curr]
        return fun(0,sum)