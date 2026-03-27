
class Solution:
    def longest(self, arr):
        # code here
        l = max(arr, key=len)
        return l