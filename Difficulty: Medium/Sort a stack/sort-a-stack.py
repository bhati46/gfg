class Solution:
    def sortStack(self, st):
        # code here 
        if len(st)==1:
            return 
        temp=st[len(st)-1]
        st.pop()
        self.sortStack(st)
        self.insert(st,temp)
    def insert(self,st,temp):
        if len(st)==0 or st[len(st)-1]<temp:
            st.append(temp)
            return 
        val=st[len(st)-1]
        st.pop()
        self.insert(st,temp)
        st.append(val)