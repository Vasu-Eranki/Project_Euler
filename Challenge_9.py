#!/bin/python3
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    product = -1
    for a in range(1,n//3):
        b = round((n**2-2*a*n)/(2*n-2*a))
        c=n-a-b
        if(a**2+b**2==c**2):
            product = max(product,a*b*c)
        else:
            pass
    print(product)

