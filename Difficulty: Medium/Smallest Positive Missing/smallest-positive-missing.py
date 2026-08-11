class Solution:
    def missingNumber(self, arr):
        # code here
        x=-1
        i=0
        while x<0:
            i+=1
            if i not in arr:
                return i