class Solution:
    def rowSum(self, mat):
        # Code here
        y=[]
        for row in mat:
            x=sum(row)
            y.append(x)
        return y