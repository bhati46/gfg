class Solution:
    def fibonacciNumbers(self, n):
        # code here
        mod=10**9+7
        dp=[-1]*(n+1)
        dp[0]=0
        dp[1]=1
        def fun(n):
            if n==0:
                return 0
            if n==1:
                return 1
            if dp[n] !=-1:
                return dp[n]
            dp[n]=(fun(n-1)+fun(n-2))%mod
            return dp[n]
        fun(n)
        return dp
        