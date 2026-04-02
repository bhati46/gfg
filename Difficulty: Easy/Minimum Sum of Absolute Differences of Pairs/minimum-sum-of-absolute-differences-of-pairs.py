#User function Template for python3

class Solution:
    def findMinSum(self, A,B,N):
        A.sort()
        B.sort()
        x=0
        for i in range(N):
            x += abs(A[i] - B[i])
        return x