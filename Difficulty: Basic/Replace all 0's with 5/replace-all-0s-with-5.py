# Function should return an integer value
class Solution:
    def convertFive(self, n):
        # Code here
        x=str(n)
        y=""
        for i in x:
            if i=="0":
                y+="5"
            else:
                y+=i
        return int(y)