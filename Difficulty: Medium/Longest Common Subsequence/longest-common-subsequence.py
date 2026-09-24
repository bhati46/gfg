class Solution:
    def lcs(self, s1, s2):
        # code here
        dp=[[-1]*len(s2) for _ in range(len(s1))]
        def fun(i,j):
            if i==len(s1) or j==len(s2):
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            take=0
            if s1[i]==s2[j]:
                take=1+fun(i+1,j+1)
            else:
                take=max(fun(i+1,j),fun(i,j+1))
            dp[i][j]=take
            return dp[i][j]
        return fun(0,0)