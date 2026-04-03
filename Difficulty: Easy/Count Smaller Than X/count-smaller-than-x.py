#User function Template for python3

class Solution:
    def smallerThanX(self,arr,n,x):
        #return required ans
        #code here
        ans=0
        for i in range(n):
            if arr[i]<x:
                ans+=1
        return ans
                