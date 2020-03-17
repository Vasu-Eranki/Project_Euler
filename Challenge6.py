#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    x = n*(n+1)*0.5 
    y = x*(2*n+1)/3
    x=x**2
    diff = int(x-y)
    print(diff) 
