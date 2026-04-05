class Solution:
    def repeatingCharacter(self,s):
        #code here
        for i in s:
            if s.count(i)>1:
                return s.index(i)
        return -1