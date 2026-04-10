class Solution:
    def twoSum(self, arr, target):
        #code here
        n = len(arr)
        l = 0
        r = n - 1
        while l < r:
            s = arr[l] + arr[r]
            if s == target:
                return [l+1, r+1]
            elif s < target:
                l += 1
            else:
                r -= 1
        return [-1, -1]