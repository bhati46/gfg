#User function Template for python3

class Solution:

    def findMinDiff(self, arr,M):
        # code here
        n=len(arr)
        arr.sort()
        x=float('inf')
        for i in range(n - M + 1):
            x = min(x, arr[i + M - 1] - arr[i])
        
        return x