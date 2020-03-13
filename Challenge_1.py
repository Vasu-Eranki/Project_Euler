#!/bin/python3

import sys
import math

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    x = n-1 
    n_3 = int(x/3)
    n_5 = int(x/5)
    n_15 = int(x/15)
    total =3*(n_3)*(n_3+1)+5*(n_5)*(n_5+1)-15*(n_15)*(n_15+1)
    total = total>>1
    print(int(total))
