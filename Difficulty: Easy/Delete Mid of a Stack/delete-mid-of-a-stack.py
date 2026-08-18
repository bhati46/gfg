class Solution:
    def deleteMid(self, s):
        # code here
        mid=len(s)//2
        self.removemid(s,mid)
        return s
    def removemid(self,s,mid):
        if mid==0:
            s.pop()
            return 
        temp=s.pop()
        self.removemid(s,mid-1)
        s.append(temp)