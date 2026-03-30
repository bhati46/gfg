#User function Template for python3

class Solution:
    def findIndex(self, arr, x):
        #code
        for i in range(len(arr)-1,-1,-1): 
            if arr[i]==x:
                return i+1
        return -1