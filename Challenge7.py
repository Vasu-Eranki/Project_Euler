#!/bin/python3
from collections import deque
import math
def prime(n):
    x =[2,3,5,7,11,13,17,19,23,29]
    if(n<len(x)):
        return x[n-1]
    else:
        upper_limit = round(n*(ln(n)+ln(ln(n))))
        x = deque(x,maxlen = upper_limit-n//2)
        gross = [i for i in range(31,upper_limit,2)]
        for i in gross:
            if(check(i)):
                x.append(i)
        return x[n-1]
def ln(x):
    e = math.e
    return math.log(x,e)
def check(x):
    flag =1
    if (x%2==0): return False
    for j in range(3,int(x**0.5)+1,2):
        if(x%j==0):
            flag = 0
            break
    return True if flag==1 else False
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    result = prime(n)
    print(result)
