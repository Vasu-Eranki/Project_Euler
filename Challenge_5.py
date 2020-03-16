#!/bin/python3
import math 
def lcm(x):
    lc = x[0]
    for i in x[1:]:
        lc = (lc*i)//math.gcd(lc,i)
    return lc

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    x = [i for i in range(1,n+1)]
    result = lcm(x)
    print(result)
