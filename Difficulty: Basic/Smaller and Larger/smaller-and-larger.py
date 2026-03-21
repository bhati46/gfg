#User function Template for python3
class Solution:
    def getMoreAndLess(self, arr, target):
        # code here
        c1=0
        c2=0
        for i in arr:
            if i>=target:
                c2=c2+1
            if i<=target:
                c1=c1+1
               
        return [c1,c2]