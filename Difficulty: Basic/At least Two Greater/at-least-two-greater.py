#User function Template for python3

class Solution:
    def findElements(self,arr):
        # Your code goes here
        arr.sort()
        n=len(arr)
        x=[]
        for i in range(n):
            if i<n-2:
                x.append(arr[i])
        return x
