#User function Template for python3

class Solution:
    def findIndex (self,arr, key ):
        #code here.
        x=[]
        for i in range(len(arr)):
            if arr[i]==key:
                x.append(i)
        if x:
            return [x[0], x[-1]]
        else:
            return [-1, -1]
            