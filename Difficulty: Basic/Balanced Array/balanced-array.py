#User function Template for python3


class Solution:
    # Function to find the minimum value required to balance the array.
    def min_value_to_balance(self, arr):
        # code here
        n=len(arr)
        x=0
        y=0
        for i in range(n):
            if i>=n//2:
                x+=arr[i]
            else:
                y+=arr[i]
        return abs(x-y)
            