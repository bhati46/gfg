#User function Template for python3
class Solution:
    def isPowerof3 (ob,N):
        # code here 
        for i in range(100):
            if pow(3,i)==N:
                return "Yes"
        return "No"
        