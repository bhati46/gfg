from typing import List


class Solution:
    def minimumTime(self, N : int, cur : int, pos : List[int], time : List[int]) -> int:
        # code here
        y=float('inf')
        for i in range(N):
            x=abs(pos[i]-cur)*time[i]
            y=min(y,x)
        return y

        
