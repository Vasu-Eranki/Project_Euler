#!/bin/python3
def palindrome(n):
    pal = []
    for i in range(100,round(n**0.5),1):
        for j in range(round(n**0.5)-10,999,1):
            temp = j*i
            if(temp%11==0):
                d = palindrome_checker(temp)
                if d and temp<n:
                    pal.append(temp)
                else:
                    pass
    return max(pal)

def palindrome_checker(n):
    e = list(str(n))
    f = list(reversed(e))
    if e == f:
        return True 
    else:
        False
if __name__=="__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        result = palindrome(n)
        print(result)
