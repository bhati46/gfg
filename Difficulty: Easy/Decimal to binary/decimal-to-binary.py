class Solution:
    def decToBinary(self, n):
        # code here
        x=""
        while n>0:
            x = str(n % 2) + x
            n = n // 2
        return int(x)