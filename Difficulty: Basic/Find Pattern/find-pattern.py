#User function Template for python3


def findPattern(s,p):
    #Your code below
    if p in s:
        return s.index(p)
    else:
        return -1
    