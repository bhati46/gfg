#User function Template for python3

  
def Sandwiched_Vowel(s):
    #Complete the function
    vowels = "aeiou"
    res = []

    for i in range(len(s)):
        if 0 < i < len(s) - 1 and s[i] in vowels and s[i-1] not in vowels and s[i+1] not in vowels:
            continue
        res.append(s[i])

    return "".join(res)