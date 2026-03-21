class Solution:
    def getAlternates(self, arr):
        # Code Here
        n=[]
        for i in range(len(arr)):
            if i%2==0:
                n.append(arr[i])
        return n
            